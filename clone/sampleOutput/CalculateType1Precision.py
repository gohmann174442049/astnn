import csv
import sys
pairRows=[]
def ListToDict(l):
    return dict(l)
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
#inputPath="Type1ClonesBetterAt90Threshold/type_1.csv"
inputPath="type_1.csv"
with open(inputPath, 'r') as file:
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

functionRowsDict=ListToDict(functionRows)
truePositive=0
falsePositive=0
counter=0
for pair in pairRows:
    if counter % 500==0:
        print(counter)
    counter+=1
    splitPair=pair.split(",")
    function1=None
    function2=None
    function1=functionRowsDict[splitPair[0]]
    function2=functionRowsDict[splitPair[1]]
    '''
    for check in functionRows:
        if int(check[0]) == int(splitPair[0]):
            function1=check[1]
        if int(check[0]) == int(splitPair[1]):
            function2=check[1]
        if(function1 != None and function2 != None):
            break
    else:
        raise Warning("not found!")
    '''
    if function1 == function2:
        truePositive +=1
    else:
        falsePositive+=1
print("true positives:", truePositive)
print("false positives:", falsePositive)
print(truePositive/(truePositive+falsePositive))
        
