#2447328
#3769242
#20684502
rows=[]
with open("Java_Repos_esc.xml", 'r', encoding='latin-1') as file:
    data=file.readlines()
    for inx, i in enumerate(data):
        if inx >= 20684450 and inx <= 20684550:
            if inx == 20684502:
                print("here!!!!!!!!")
            print(i)
        
