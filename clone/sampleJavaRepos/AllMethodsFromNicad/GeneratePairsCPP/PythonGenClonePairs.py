import time
import itertools as it



lines=[]
with open("IdsOnly.txt", 'r') as file:
    data= file.readlines()
    for i in data:
        lines.append(i)
start_time = time.time()
pairs=list(it.combinations(lines[0:25000],2))
print("--- %s seconds ---" % (time.time() - start_time))
print(len(pairs))
