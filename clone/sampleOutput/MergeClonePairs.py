files=[]

for i in range(1,6):
    files.append("type_"+str(i)+".csv")

clonePairs=[]
for file in files:
    with open(file, 'r') as currInput:
        data=currInput.readlines()
        for pair in data:
            clonePairs.append(pair.replace('\n', ""))

with open("ASTnn_Clone_Pairs.csv", 'w') as outputFile:
    outputFile.write("id1, id2")
    outputFile.write('\n')
    for pair in clonePairs:
        outputFile.write(pair)
        outputFile.write('\n')

