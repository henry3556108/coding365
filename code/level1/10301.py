#encoding: utf-8

def clean(ls):
    for x in range(len(ls)):
        ls.pop()
    out(ls1,ls2)

def uni(ls1,ls2):
    temp=ls2.copy()
    for x in range(len(ls2)):
        for y in range(len(ls1)):
            if(ls2[x]==ls1[y]):
                temp.remove(int(ls1[y]))
    temp=ls1+temp
    print("[",end="")
    for x in temp:
        print(x,end=",")
    print("]\n",end="")

def inside(ls,num): 
    if(int(num) in ls):
        return 1
    
def out(ls1,ls2):
    print("A:[",end="")
    for x in ls1:
        print(x,end="")
        if(len(ls1)>0): print(",",end="")
    print("]B:[",end="")
    for y in ls2:
        print(y,end="")
        if(len(ls2)>0): print(",",end="")
    print("]\n",end="")    
def combine(ls,num):
    num = int(num)
    ls.append(num)  
    out(ls1,ls2)
def intre(ls1,ls2):
    temp= ["["]
    for x in range(len(ls2)):
        if(ls2[x] in ls1): temp.append(str(ls2[x])+",")    
    temp.append("]")
    for x in temp:
        print(x,end="")
    print()
    
a=10
ls1=[]
ls2=[]

while(a!=0):
    a=input("").split(' ')
    print(a)
    if(a[0]=='0'):    break
    if (a[0]=='1'):    clean(ls1)       
    if (a[0]=='2'):    clean(ls2)
    if (a[0]=='3'):    
        if(inside(ls1,a[1])!= 1):
            combine(ls1,a[1])
        else: out(ls1,ls2)
    if (a[0]=='4'):
        if(inside(ls2,a[1])!= 1):
            combine(ls2,a[1])
        else: out(ls1,ls2)
    if (a[0]=='5'):    
        if(inside(ls1,a[1])==1):
            ls1.remove(int(a[1]))
        out(ls1,ls2)
    if (a[0]=='6'):
        if(inside(ls2,a[1])==1):
            ls2.remove(int(a[1]))
        out(ls1,ls2)    
    if (a[0]=='7'):    uni(ls1,ls2)
    if (a[0]=='8'):    intre(ls1,ls2)
    if (a[0]=='9'):    
        for x in ls1:
            if (x not in ls2):
                print('0')
                break
            else:    
                print('1')
                break
        if(len(ls1)==0): print('1')        