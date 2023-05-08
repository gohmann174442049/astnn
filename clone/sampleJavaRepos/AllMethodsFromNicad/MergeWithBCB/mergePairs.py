import csv
rows=[]
with open("bcb_clonePairs.csv", 'r') as file:
    data=csv.reader(file)
    for i in data:
        rows.append(i)
print(len(rows))
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

#for i in rows:
#    print(i)
with open("../mergedClonePairs.csv", 'w') as outputFile:
    for row in rows:
        outputFile.write(",".join(row))
        outputFile.write('\n')
        
