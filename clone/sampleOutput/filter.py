rows=[]
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

