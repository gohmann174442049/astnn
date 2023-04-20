import xml.etree.ElementTree as ET
import sys
import javalang
generatePairs=True
offset=23677151
def replace_last(source_string, replace_what, replace_with):
    head, _sep, tail = source_string.rpartition(replace_what)
    return head + replace_with + tail


def parse_program(func):
    tokens = javalang.tokenizer.tokenize(func)
    parser = javalang.parser.Parser(tokens)
    tree = parser.parse_member_declaration()


idArray=[]
tree= ET.parse("Java_Repos_sample_esc.xml")
root= tree.getroot()
baseOffset=23677151+1
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
failedParse=0
with open("sample_funcs_all.tsv", 'w', encoding='utf-8') as outputFile:
    index=0
    for func in tsvArray:
        if index % 1000 ==0:
            print(index)
        index+=1
        try:
            if func[1].count('\n') >= 10:
                formattedFun=func[1].replace("\"","\"\"")
                ### ensure it is possible to parse the function
                ### before adding it to the dataset
                try:
                    parse_program(formattedFun)
                except:
                    failedParse+=1
                    continue
                success+=1
                idArray.append(int(func[0]))
                formattedFun=replace_last(formattedFun, '\t', '')
                outputFile.write(func[0]+'\t'+"\""+ formattedFun+"\"")
                outputFile.write('\n')
        except Exception as e:
            #invalid char present
            failed+=1
            pass
print(success)
print(failed)

possiblePairs=[]
print(len(idArray))
if generatePairs==False:
    exit(1)
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
    outputPairs.write(" ,id1,id2,label")
    outputPairs.write('\n')
    index=0
    for i in pairs:
        index+=1
        if index % 1000000==0:
            print(index)
        pair=list(i)
        outputPairs.write(str(index-1)+","+str(baseOffset+pair[0])+","+str(baseOffset+pair[1])+",0")
        outputPairs.write('\n')
