#encoding: utf-8
data={}
cac={}
time=[]
temp=[]
ndata=[]
list=[]
store=[]
def judge(city,dict,temp):
    ndata=[]
    for x in range(len(temp)):
        ndata=city[int(temp[x])]
        list=city[ndata[x]].copy()
        print(type(ndata[0]),type(list[0]))
        for y in range(len(ndata)):
            store.append(list[x].append(ndata[y]))
    print(store,ndata,list)

ndata=input("input:").split(",")
for x in ndata:
    x=int(x)
    time.append(x)
ndata=[]
print(time)
for x in range(time[0]):
    data[x+1]=[]
    
print(data)
for x in range(1,time[1]+1,1):
    temp=input("input:").split(",")
    ndata=[]
    for i in temp:
        ndata.append(int(i))
    data[ndata[0]].append(ndata[1])
    data[ndata[1]].append(ndata[0])
    cac[ndata[0],ndata[1]]=ndata[2]
    cac[ndata[1],ndata[0]]=ndata[2]
    temp=['1']
print(data,cac,temp)
print(ndata,list)
for x in range(time[0]-1):
    judge(data,cac,temp)


judge(data,cac)


