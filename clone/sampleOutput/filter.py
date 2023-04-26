rows=[]
'''
with open("type_1.csv", 'r') as file:
    data=file.readlines()
    print(len(data))
    for i in data:
        splitting=i.split(",")
        if int(splitting[0])> 23677150 and int(splitting[1]) > 23677150:
            rows.append(i)
        if (int(splitting[0]) == 23768492) and (int(splitting[0]) == 23768496):
            print(i)
print(len(rows))
'''
with open("trainingData.csv", 'r') as file:
    data=file.readlines()
    print(len(data))
    index=0
    for i in data:
        if index==0:
            index+=1
            continue
        splitting=i.split(",")
        if int(splitting[1])> 23677150 or int(splitting[2]) > 23677150:
            rows.append(i)
        if (int(splitting[1]) == 520600) and (int(splitting[2]) == 888827):
            print(i)
print(len(rows))
testCount=0
with open("testingData.csv", 'r') as file:
    data=file.readlines()
    print(len(data))
    index=0
    for i in data:
        if index==0:
            index+=1
            continue
        splitting=i.split(",")
        if int(splitting[3]) == -1:
            testCount +=1
        else:
            print(splitting[3])
        if int(splitting[1])> 23677150 or int(splitting[2]) > 23677150:
            rows.append(i)
        if (int(splitting[1]) == 23768492) and (int(splitting[2]) == 23768496):
            print(i)
print(len(rows))
