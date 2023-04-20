xmlLines=[]
with open("java-repos_functions_sample.xml" , 'r', encoding='latin-1') as file:
    lines=file.readlines()
    for i in lines:
        xmlLines.append(i)

ignoreTags=["<source file", "</source>"+'\n']
newXMLLines=[]
counter=0
print("total: "+ str(len(xmlLines)))

for line in xmlLines:
    validTag=False
    if counter % 10000 == 0:
        print(counter)
    counter+=1
    #if counter >=2073060 and counter <=2073100:
    #    print(line, end='')
    for tag in ignoreTags:
        if tag in line:
            validTag=True
            newXMLLines.append(line)
            break    
    if validTag==False:
        temp=line
        temp=temp.replace( "&", "&amp;")
        temp=temp.replace("\"", "&quot;")
        temp=temp.replace("'", "&apos;")
        temp=temp.replace("<", "&lt;")
        temp=temp.replace(">", "&gt;")
        newXMLLines.append(temp)

with open("Java_Repos_sample_esc.xml" , 'w', encoding='latin-1') as file:
    for i in newXMLLines:
        file.write(i)
    
