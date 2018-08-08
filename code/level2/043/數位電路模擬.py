def output(x):
    ls=[]
    for y in range(3,-1,-1):
        if x>=2**y:
            x-=2**y
            ls.append('1')
        else: ls.append('0')
    for y in ls:
        print(y,end="")
    print("")
def run(value):
    for x in range(0,9):
        if value>1:
            if value%2==0:
                value=int(value/2)
            else:
                value+=1
                value=int(value/2)
        else:
            break
    output(x)

    
    
def ten(inpu):
    sum=0
    ls=[]
    for x in inpu:
        ls.append(x)
    ls.reverse()
    for x in range(0,len(ls)):
        sum=sum+(int(ls[x])*(2**x))
    return sum

def main():
    while True:
        inpu=input("")
        if inpu=='-1':
            break
        elif inpu=="0":
            pass
        elif inpu not in "-1,0": run(ten(inpu))

    
if __name__=='__main__':
    main()
    