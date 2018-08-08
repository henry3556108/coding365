#encoding: utf-8

ls=[]
flag=0
b=input("")
a=b.split(' ')
count=0
if(a[0]=='1'):flag='1'
if(a[0]=='2'):
    flag='2'
    count=count+1



while( count <= 5):
    b=input("")
    a=b.split(' ')
    if(a[0]=='2'):
        count=count-1
        if(count==0):
            print("EMPTY")
            break
        if(flag=='1'):
            ls.pop()
        if(flag=='2'):
            ls.reverse()
            ls.pop()
            ls.reverse()
    if(a[0]=='3'):
        for x in ls:
            print(x,end=" ")
        break
    if(count==5):
        print("FULL")
        break
    
    if(a[0]=='1'):
        ls.append(a[1])
        count=count+1
    if(a[0]=='3'):
        for x in ls:
            print(x,end=" ")
    
    
        