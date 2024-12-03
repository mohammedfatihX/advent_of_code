import statistics

counter=0

def condition(monlist):
    length=len(monlist)
    resultlist=[]
    topres=True
    for i in range(length):
        if( i < length-1):
            defr=monlist[i]-monlist[i+1]
            mybool=defr>0
            res = 3-abs(defr)
            if (res < 0 or res == 3) or (len(resultlist)!= 0 and resultlist[-1] != mybool) :
                topres =False

            resultlist.append(mybool)

            
       
    return topres


with open('input.txt','r') as f:
    for line in f:
        
        counter = counter+1 if condition(list(map(lambda x:int(x),line.split(' ')))) else counter

print(counter)