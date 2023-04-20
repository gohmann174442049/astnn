import xml.etree.ElementTree as ET
import sys

def replace_last(source_string, replace_what, replace_with):
    head, _sep, tail = source_string.rpartition(replace_what)
    return head + replace_with + tail
idArray=[]
tree= ET.parse("Java_Repos_sample_esc.xml")
root= tree.getroot()
id_func=23677151+1
for i in root.getchildren():
    i.attrib.update({"id": str(id_func)})
    #idArray.append(id_func)
    id_func+=1

tsvArray=[]
for i in root.getchildren():
    currId=i.attrib['id']
    body= i.text
    tsvArray.append([currId, body])

#for i in range(0, 10):
#    print(tsvArray[i])
success=0
failed=0
with open("sample_funcs_all.tsv", 'w', encoding='latin-1') as outputFile:
    for func in tsvArray:
        #print(func)
        try:
            if func[1].count('\n') >= 10:
                success+=1
                idArray.append(int(func[0]))
                formattedFun=func[1].replace('\n',"\n\t").replace("\"","\"\"")
                formattedFun=replace_last(formattedFun, '\t', '')
                outputFile.write(func[0]+'\t'+"\""+ formattedFun+"\"")
                outputFile.write('\n')
        except Exception as e:
            #print(e)
            #invalid char present
            failed+=1
            pass
print(success)
print(failed)

possiblePairs=[]
print(len(idArray))
'''
for i in range(0, len(idArray)):
    if i % 10==0:
        print(i)
    for j in range(i, len(idArray)):
        possiblePairs.append([idArray[i], idArray[j]])
print(len(possiblePairs))
'''
import itertools as it
n= len(idArray)
pairs=list(it.combinations(range(n),2))
print(len(pairs))
print("writing...")
with open("possiblePairs.csv", 'w') as outputPairs:
    outputPairs.write("id1,id2,clone")
    outputPairs.write('\n')
    index=0
    for i in pairs:
        index+=1
        if index % 100000==0:
            print(index)
        pair=list(i)
        outputPairs.write(str(pair[0])+","+str(pair[1])+",0")
        outputPairs.write('\n')
