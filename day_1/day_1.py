from functools import reduce
rights=[]
lefts=[]
results=[]
re= lambda x,y:x+y

with open('input.txt','r') as f:
    for line in f:
        tempLeft,tempRight= line.strip().split('   ')
        rights.append(int(tempRight))
        lefts.append(int(tempLeft))
        
rights.sort()
lefts.sort()
for i in range(len(rights)):
    results.append(abs(lefts[i]-rights[i]))

res =reduce(re,results)
print(res)

    

      


