
def max():
    inpu=input("")
    if int(inpu)%2==0:
        max = int(inpu)/2
    elif int(inpu)%2==1:
        max = (int(inpu)+1)/2
        max = int(max)
    return max
    
def output(style,max):
    if style=="2":
        for x in range(1,max+1,1):
            for z in range(max,x,-1):
                print(".",end="")
            for y in range(x,0,-1):
                print(y,end="")
            print("")
        for x in range(max-1,0,-1):
            for z in range(max,x,-1):
                print(".",end="")
            for y in range(x,0,-1):
                print(y,end="")
            print("")
            
    elif style=='1':
        for x in range(1,max+1,1):
            for y in range(1,x+1,1):
                print(y,end="")
            print("")
        for x in range(max-1,0,-1):
            for y in range(1,x+1,1):
                print(y,end="")
            print("")
    
def main():
    style=input("")
    nmax=int(max())
    output(style,nmax)

if __name__=='__main__':
    main()