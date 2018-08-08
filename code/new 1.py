#encoding: utf-8

ctc={}
data={}
inpu=[]
time=[]
temp2=[]
ls=[]
temp=[['1']]
store=[]
a=0

def judge(ctc, data, temp,a):
    for x in temp:
        temp2=x[-1]
        a=a+len(data[temp2])
        ls=data[temp2].copy()
        for y in range(a):
            store.append(x)
            store[y].append(ls[y])
            print(store)
    

    
inpu=input("input:").split(",")
for x in inpu:
    time.append(x)

for x in range(int(time[0])):
    data[str(x+1)]=[]

    
print(data)
for x in range(1,int(time[1])+1,1):
    inpu=input("input:").split(",")
    data[inpu[0]].append(inpu[1])
    data[inpu[1]].append(inpu[0])
    ctc[inpu[0],inpu[1]]=int(inpu[2])
    ctc[inpu[1],inpu[0]]=int(inpu[2])

print(data,ctc)
judge(ctc, data, temp,a)
