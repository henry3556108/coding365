#encoding: utf-8


def whobig(ls,a):
    if(len(ls)==0): return 0
    ls_size=mysize(ls[-1])
    a_size=mysize(a)
    if(a_size>ls_size): return 0
    else: return 1
  
def mysize(a):
    if(a=='+'or a=='-'): return 1
    if(a=='*'or a=='/'): return 2
    if(a=='^'): return 3
    if(a=='('): return 0
        

def judge(temp,num):
    if(x in "+-*/^"):
        while(whobig(temp,num)==1):
            output.append(temp[-1]) 
            temp.pop()
        if(whobig(temp,num)==0):
            temp.append(num)
    elif x == '(': temp.append(num)
    elif x == ')': 
        for y in reversed(temp):
            if y=='(':
                temp.pop()
                break
            else: 
                output.append(y)
                temp.pop()

output=[]
temp=[]
data=[]
b=input("")
for x in b:
    data.append(x)

for x in data:
    if(x.isalpha()==1): output.append(x)
    else: judge(temp,x)
for x in reversed(temp):
    output.append(x)
for x in output:
    print(x,end="")
    