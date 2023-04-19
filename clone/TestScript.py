import pandas as pd
import torch
import time
import numpy as np
import warnings
from gensim.models.word2vec import Word2Vec
from model import BatchProgramCC
from torch.autograd import Variable
from sklearn.metrics import precision_recall_fscore_support

root = 'data/'
lang='java'
if lang == 'java':
    categories = 5
print("Train for ", str.upper(lang))
full_data= pd.read_pickle(root+lang+'/train/blocks.pkl')
train_data = full_data.sample(frac=1)
test_data = full_data.sample(frac=1)
