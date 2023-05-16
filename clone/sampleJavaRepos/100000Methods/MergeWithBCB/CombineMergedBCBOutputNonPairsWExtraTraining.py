import csv
import itertools
from collections import Counter

def check_duplicate_rows(my_list):
    seen = set()
    for row in my_list:
        row_tuple = tuple(tuple(sublist) for sublist in row)
        if row_tuple in seen:
            return True
        seen.add(row_tuple)
    return False
# Specify the paths to your CSV files
csv_file1 = 'mergedBCBOutputNonPairs.csv'
csv_file2 = 'bcb_clonePairs_more_training.csv'

#csv_file2 = 'bcb_clonePairs_more_training.csv'
finalCSV=[]
with open(csv_file1, 'r') as orig, open(csv_file2, 'r') as moreTraining:
    origData=csv.reader(orig)
    index=0
    adding=False
    moreTrainingData=csv.reader(moreTraining)
    finalCSV=list(moreTrainingData)
    print(len(finalCSV))
    for row in origData:
        if index==97535:
            print(row)
            adding=True
            index+=1
            continue
        if adding:
            finalCSV.append(row)
        index+=1
print(len(finalCSV))
for i in range(0,10):
    print(finalCSV[i])

with open("mergedBCBOutputNonPairs_mTraining.csv", 'w') as file:
    for i in finalCSV:
        file.write(",".join(i))
        file.write('\n')


print(check_duplicate_rows(finalCSV))

'''
print(len(finalCSV))
#finalCSV = list(set(finalCSV))
newFinalCSV = [x for i, x in enumerate(finalCSV) if x not in finalCSV[:i]]
#counter = Counter(finalCSV)
#newFinalCSV = list(counter.keys())
print(len(newFinalCSV))
for i in range(0,25):
    print(newFinalCSV[i])

with open("mergedBCBOutputNonPairs_more_training.csv", 'w') as outputFile:
    for pair in newFinalCSV:
        outputFile.write(",".join(pair))
        outputFile.write('\n')
'''
