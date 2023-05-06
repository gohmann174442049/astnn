headers=[]
bcbClones=[]
import csv
with open("bcb_clonePairs.csv" , 'r') as file:
    data= csv.reader(file)
    index=0
    for i in data:
        if index ==0:
            index+=1
            headers.append(i)
            continue
        bcbClones.append(i)
for i in range(0, 10):
    print(bcbClones[i])

outputExtraNonPairs=[]
index=0
with open("OutputExtraNonPairs.csv", 'r') as extrasFile:
    data = csv.reader(extrasFile)
    for i in data:
        if index ==0:
            index+=1
            continue
        outputExtraNonPairs.append(i)
print("----")
for i in range(0, 10):
    print(outputExtraNonPairs[i])

with open("mergedBCBOutputNonPairs.csv", 'w') as output:
    output.write(",".join(headers[0]))
    output.write('\n')
    for i in bcbClones:
        output.write(",".join(i))
        output.write('\n')
    for i in outputExtraNonPairs:
        output.write(",".join(i))
        output.write('\n')
