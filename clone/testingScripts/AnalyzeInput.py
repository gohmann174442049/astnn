import csv
import pandas
rows=[]
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
with open(r"..\data\java\bcb_funcs_all.tsv", 'r', encoding='latin-1') as inputFile:
    data=csv.reader(inputFile, delimiter= '\t', quotechar = "\"")
    for i in data:
        #print(i[1][1:10])
        rows.append(i)
#data = pandas.read_csv(r"..\data\java\bcb_funcs_all.tsv")
print(len(rows))
