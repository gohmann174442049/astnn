import csv
import pandas
rows=[]
rowsBCB=[]
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
with open(r"bcb_funcs_all.csv", 'r', encoding='utf-8') as inputFile:
    data=csv.reader(inputFile, delimiter= '\t', quotechar = "\"")
    for i in data:
        #print(i[1][1:10])
        rows.append(i)
print(len(rows))
#for i in range(0, 10):
#    print(rows[i])
rowsSample=[]
with open(r"../sample_funcs_all.tsv", 'r', encoding='utf-8') as inputFile:
    data=csv.reader(inputFile, delimiter= '\t', quotechar = "\"")
    for i in data:
        #print(i[1][1:10])
        rows.append(i)
print(len(rows))
with open(r"../merged_dataset_funcs_all.tsv", 'w', encoding='utf-8') as outputFile:
    for func in rows:
        outputFile.write(func[0]+'\t'+"\""+func[1].replace("\"", "\"\"")+"\"")
        outputFile.write('\n')
