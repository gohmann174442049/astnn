import csv
import sys
pairRows=[]
def SetFieldSizeLimit():
    maxInt = sys.maxsize

    while True:
        # decrease the maxInt value by factor 10 
        # as long as the OverflowError occurs.

        try:
            csv.field_size_limit(maxInt)
            break
        except OverflowError:
            maxInt = int(maxInt/10)
SetFieldSizeLimit()
with open("type_1.csv", 'r') as file:
    data=file.readlines()
    print(len(data))
    for i in data:
        splitting=i.split(",")
        if int(splitting[0])> 23677150 and int(splitting[1]) > 23677150:
            pairRows.append(i.replace('\n', ""))
print(len(pairRows))

functionRows=[]
with open("../data/java/merged_dataset_funcs_all.tsv", 'r', encoding='latin-1') as inputFuncs:
    data=csv.reader(inputFuncs, delimiter='\t', quotechar="\"")
    for i in data:
        functionRows.append(i)
#for i in range(0,10):
#print(functionRows[i])
truePositive=0
falsePositive=0
counter=0
for pair in pairRows:
    if counter % 10000==0:
        print(counter)
    counter+=1
    splitPair=pair.split(",")
    function1=None
    function2=None
    for check in functionRows:
        if(function1 != None and function2 != None):
            break
        if int(check[0]) == int(splitPair[0]):
            function1=check[1]
        if int(check[0]) == int(splitPair[1]):
            function2=check[1]
    else:
        raise Warning("not found!")
    if function1 == function2:
        truePositive +=1
    else:
        falsePositive+=1
print(truePositive)
print(falsePositive)
print(truePositive/(truePositive+falsePositive))
        
