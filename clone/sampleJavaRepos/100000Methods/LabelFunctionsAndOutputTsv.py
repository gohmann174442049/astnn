import xml.etree.ElementTree as ET
import sys

tree= ET.parse("Java_Repos_sample_esc.xml")
root= tree.getroot()
id=23677151+1
for i in root.getchildren():
    i.attrib.update({"id": str(id)})
    id+=1

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
                outputFile.write(func[0]+'\t'+"\""+ func[1]
                                 .replace("\"","\"\"").replace('\n',"\n\t"+"\""))
                outputFile.write('\n')
        except:
            #invalid char present
            failed+=1
            pass
print(success)
print(failed)
