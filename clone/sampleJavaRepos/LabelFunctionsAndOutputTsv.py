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

for i in range(0, 10):
    print(tsvArray[i])
