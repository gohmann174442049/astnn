import csv
rows=[]
with open("bcb_clonePairs.csv", 'r') as file:
    data=csv.reader(file)
    for i in data:
        rows.append(i)
print(len(rows))
with open("bcb_clonePairs.csv", 'r') as file:
    data=csv.reader(file)
    index=0
    for i in data:
        if index==0:
            index+=1
            continue
        rows.append(i)
print(len(rows))
#for i in rows:
#    print(i)
with open("../mergedClonePairs.csv", 'w') as outputFile:
    for row in rows:
        outputFile.write(",".join(row))
        
