import csv
import sys
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
ids=[]
with open(r"bcb_funcs_all.csv", 'r', encoding='utf-8') as inputFile:
    data=csv.reader(inputFile, delimiter= '\t', quotechar = "\"")
    for i in data:
        ids.append(i[0])
print(len(ids))

originalPairs=[]
with open(r"bcb_clonePairs.csv", 'r', encoding='utf-8') as inputFile:
    data=csv.reader(inputFile, delimiter= ',')
    index=0
    for i in data:
        if index==0:
            index+=1
            continue
        originalPairs.append(i)
for i in range(0, 10):
    print(originalPairs[-i])
import itertools as it
newPairs=list(it.combinations(ids[:500],2))
print(len(newPairs))
#1:3
print("generating pairs...")
combinePairs=[]
for pair in originalPairs:
    combinePairs.append(pair)
lastIndex=97534 + 1
counter=0
print("start gnerating new Pairs")
for newPair in newPairs:
    if counter % 500 == 0:
        print("count", str(counter), str(len(newPairs)))
    counter+=1
    for checkPair in combinePairs:
        if ((int(checkPair[1]) == int(newPair[0]) and int(checkPair[2]) == int(newPair[1])) or
            (int(checkPair[1]) == int(newPair[1]) and int(checkPair[2]) == int(newPair[0]))):
            #print(checkPair)
            break
    else:
        combinePairs.append([str(lastIndex), str(newPair[0]), str(newPair[1]), '0'])
        lastIndex+=1

with open(r"all_bcb_clonePairs.csv", 'w', encoding ='utf-8') as outputFile:
    for row in combinePairs:
        _=outputFile.write(",".join(row))
        _=outputFile.write('\n')
