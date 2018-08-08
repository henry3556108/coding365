import numpy
ls=[]

def temp(empt,x):
    ls=empt[-1]
    empt.insert(x,ls)
    empt.pop()
    return empt

def GetDetermin(empt,x):
    thels=[]
    thels=temp(empt,x)
    for x in range(len(thels)):
        for y in range(len(thels)):
            
            thels[x][y]=int(thels[x][y])
    a=int(numpy.linalg.det(thels))
    return a

def GetDelta(ls):
    nls=[]
    temp=[]
    empt=[]
    for x in range(len(ls[0])):
        temp.append(empt)
    for x in ls:
        for y in range(len(x)):
            empt=temp[y].copy()
            empt.append(x[y])
            temp[y]=empt
            empt=[]
    for x in range(len(temp)):
        empt=temp.copy()
        del empt[x]
        nls.append(GetDetermin(empt,x))
    return nls
def GetValue(ls):
    nls=[]
    temp=[]
    nls=GetDelta(ls)
    for x in range(len(nls)-1):
        temp.append(str(int(nls[x]/nls[-1])))
    for x in range(len(temp)):
        print("X[{a}]={b}".format(a=x+1,b=temp[x]))
    

def main():
    inpu=input("")
    for x in range(int(inpu)):
        ninpu=input("").split(" ")
        nls=[]
        for y in ninpu:
            nls.append(y)
        ls.append(nls)
    GetValue(ls)
    
if  __name__=='__main__':
    main()
