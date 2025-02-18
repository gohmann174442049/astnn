import pandas as pd
import torch
import time
import numpy as np
import warnings
from gensim.models.word2vec import Word2Vec
from model import BatchProgramCC
from torch.autograd import Variable
from sklearn.metrics import precision_recall_fscore_support
warnings.filterwarnings('ignore')


def WritePredicts(test_data_t,probability, t):
    test_data_t["probability"]=probability
    test_data_t=test_data_t.drop("label", axis=1)
    test_data_t=test_data_t.drop("code_x", axis=1)
    test_data_t=test_data_t.drop("code_y", axis=1)
    test_data_t.to_csv("sampleOutput\\predicts_"+str(t)+".csv")

def get_batch(dataset, idx, bs):
    tmp = dataset.iloc[idx: idx+bs]
    x1, x2, labels = [], [], []
    for _, item in tmp.iterrows():
        x1.append(item['code_x'])
        x2.append(item['code_y'])
        labels.append([item['label']])
    return x1, x2, torch.FloatTensor(labels)


if __name__ == '__main__':
    '''
    import argparse

    parser = argparse.ArgumentParser(description="Choose a dataset:[c|java]")
    parser.add_argument('--lang')
    args = parser.parse_args()
    if not args.lang:
        print("No specified dataset")
        exit(1)
    root = 'data/'
    lang = args.lang
    categories = 1
    '''
    root = 'data/'
    lang='java'
    if lang == 'java':
        categories = 5
    print("Train for ", str.upper(lang))
    train_data = pd.read_pickle(root+lang+'/train/blocks.pkl').sample(frac=1)
    test_data = pd.read_pickle(root+lang+'/test/blocks.pkl').sample(frac=1)

    word2vec = Word2Vec.load(root+lang+"/train/embedding/node_w2v_128").wv
    MAX_TOKENS = word2vec.syn0.shape[0]
    EMBEDDING_DIM = word2vec.syn0.shape[1]
    embeddings = np.zeros((MAX_TOKENS + 1, EMBEDDING_DIM), dtype="float32")
    embeddings[:word2vec.syn0.shape[0]] = word2vec.syn0

    HIDDEN_DIM = 100
    ENCODE_DIM = 128
    LABELS = 1
    EPOCHS = 15
    BATCH_SIZE = 64
    USE_GPU = True

    model = BatchProgramCC(EMBEDDING_DIM,HIDDEN_DIM,MAX_TOKENS+1,ENCODE_DIM,LABELS,BATCH_SIZE,
                                   USE_GPU, embeddings)
    if USE_GPU:
        model.cuda()

    parameters = model.parameters()
    optimizer = torch.optim.Adamax(parameters)

    #num_samples_class1 = 350
    #num_samples_class2 = 999650
    #weight_class1 = 1.0 / num_samples_class1
    #weight_class2 = 1.0 / num_samples_class2
    #class_weights = torch.tensor([weight_class1, weight_class2])
    #loss_function = torch.nn.BCELoss(weight=class_weights)
    
    loss_function = torch.nn.BCELoss()

    print(train_data)
    precision, recall, f1 = 0, 0, 0
    print('Start training...')
    #for t in range(1, categories+1):
    for t in range(1, categories+1):
        print("clone type:", t)
        # subset the data to train for each given type on bigclonebench
        train_data_t = train_data[train_data['label'].isin([t, 0])]
        train_data_t.loc[train_data_t['label'] > 0, 'label'] = 1
        
        #only test the unknown data
        test_data_t = test_data[test_data['label'].isin([-1])]
        #test_data_t = test_data[test_data['label'].isin([t, 0])]
        test_data_t.loc[test_data_t['label'] > 0, 'label'] = 1

        print("test Data Type")
        #print(type(test_data))
        # training procedure
        for epoch in range(EPOCHS):
            start_time = time.time()
            # training epoch
            total_acc = 0.0
            total_loss = 0.0
            total = 0.0
            i = 0
            print(len(train_data_t))
            while i < len(train_data_t):
                #print(str(i)+ " of "+ str(len(train_data_t)))
                batch = get_batch(train_data_t, i, BATCH_SIZE)
                i += BATCH_SIZE
                train1_inputs, train2_inputs, train_labels = batch
                if USE_GPU:
                    train1_inputs, train2_inputs, train_labels = train1_inputs, train2_inputs, train_labels.cuda()

                model.zero_grad()
                model.batch_size = len(train_labels)
                model.hidden = model.init_hidden()
                output = model(train1_inputs, train2_inputs)

                loss = loss_function(output, Variable(train_labels))
                #print("training loss:", loss)
                loss.backward()
                optimizer.step()
        print("Testing-%d..."%t)
        # testing procedure
        #probablity is used to output the neural network predicts to assess precision and recall
        #remove this metric when NN is tuned and being run on the full set of data.
        probability=[]
        predicts = []
        trues = []
        total_loss = 0.0
        total = 0.0
        i = 0
        while i < len(test_data_t):
            print(i, len(test_data))
            batch = get_batch(test_data_t, i, BATCH_SIZE)
            i += BATCH_SIZE
            test1_inputs, test2_inputs, test_labels = batch
            if USE_GPU:
                test_labels = test_labels.cuda()

            model.batch_size = len(test_labels)
            model.hidden = model.init_hidden()
            output = model(test1_inputs, test2_inputs)

            loss = loss_function(output, Variable(test_labels))
            # calc testing acc
            predicted = (output.data > 0.95).cpu().numpy()
            #notEncodedData= (output.data > 0.5)   
            predicts.extend(predicted)
            #append data for output
            probability.extend((output.data).cpu().numpy())

            trues.extend(test_labels.cpu().numpy())
            total += len(test_labels)
            total_loss += loss.item() * len(test_labels)
        assert len(test_data_t)==len(predicts)
        WritePredicts(test_data_t, probability, t)
        idPairs=[]
        count=0
        for row in test_data_t.itertuples():
            if predicts[count]==True:
                idPairs.append([str(row[1]), str(row[2])])
            count+=1
        with open("sampleOutput\\type_"+str(t)+".csv", 'w') as file:
            for pair in idPairs:
                file.write(",".join(pair))
                file.write('\n')
        '''
        weights = [0, 0.005, 0.001, 0.002, 0.010, 0.982]
        p, r, f, _ = precision_recall_fscore_support(trues, predicts, average='binary')
        precision += weights[t] * p
        recall += weights[t] * r
        f1 += weights[t] * f
        print("Type-" + str(t) + ": " + str(p) + " " + str(r) + " " + str(f))
        '''

    #print("Total testing results(P,R,F1):%.3f, %.3f, %.3f" % (precision, recall, f1))
    print("finished YAY!")