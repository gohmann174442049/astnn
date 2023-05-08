import csv
import random
header=None
nonPairRows=[]
rows=[]
with open("mergedBCBOutputNonPairs.csv", 'r') as file:
    data=csv.reader(file)
    index = 0
    for i in data:
        if index ==0:
            index+=1
            header=i
            continue
        if index < 100000:
            rows.append(i)
        else:
            nonPairRows.append(i)
        index +=1
        
rows=rows+random.sample(nonPairRows, 325000)
rows.insert(0, header)
print(len(rows))
for i in range(0,10):
    print(rows[i])
print("...")
for i in range(1,11):
    print(rows[-i])
with open("../possiblePairs.csv", 'r') as file:
    data=csv.reader(file)
    index=0
    for i in data:
        if index==0:
            index+=1
            continue
        index+=1
        rows.append(i)
print(index-1)
print(len(rows))
tuple_list = [tuple(x) for x in rows]
if len(tuple_list) == len(set(tuple_list)):
    "no repeats!"
#for i in rows:
#    print(i)
with open("../mergedClonePairs.csv", 'w') as outputFile:
    index=0
    outputFile.write(",".join(rows[0]))
    outputFile.write('\n')
    for row in rows[1:]:
        outputFile.write(str(index)+","+",".join(row[1:]))
        outputFile.write('\n')
        index+=1
        
