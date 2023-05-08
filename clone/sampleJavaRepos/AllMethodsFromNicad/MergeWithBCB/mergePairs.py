import csv
import random
import itertools

header=None
nonPairRows=[]
rows=[]
with open("mergedBCBOutputNonPairs.csv", 'r') as file1, open("../possiblePairs.csv", 'r') as file2, open("../mergedClonePairs.csv", 'w', newline='') as outputFile:
    print("read in bcb pairs")
    bcbRows=itertools.islice(csv.reader(file1), 425000)
    #print(len(bcbRows))
    print("read in data...")
    datarows=csv.reader(file2)
    #print(len(datarows))
    next(datarows)
    print("combining...")
    combined_reader = itertools.chain(bcbRows, datarows)
    print("write both out as csv")
    writer=csv.writer(outputFile)
    for row in combined_reader:
        writer.writerow(row)
