import pymysql

def GetAvg(dic):
    avg=[]
    for x in dic:
        temp=[]
        sum=0
        temp=dic[x].copy()
        for x in temp:
            sum=sum+int(x[2])
        avg.append(str(int(sum/len(temp))))
    return avg
    
def GetOverAvg(dic,avg):
    ls=[]
    _=0
    for x in dic:
        ls.append(x)
        for y in dic[x]:
            if int(y[2])>= int(avg[_]):
                ls.append(y[0] and y[1])            
        _=_+1
    for x in dic:
        print("Class {} {} students are : ".format("over average",x),end="")
        for y in dic[x]:
            if y[1] in ls:
                print(y[1],end=" ")
        print()
            
def GetDB():    
    db = pymysql.connect("192.168.194.132","root","root","hwdb")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Data")
    data = cursor.fetchall()
    return data
    
def MostStudent(dic,a):
    nls=[]
    temp=[]
    for _ in range(a):
        top=0
        prt=None
        for x in dic:
            temp=dic[x].copy()
            if len(temp)>=top and x not in nls:
                top=len(temp)
                prt=x
        nls.append(prt)
        
    print("Has most student top {}: ".format(a),nls)

def GetAllFail(dic):
    temp=[]
    allfail=[]
    for x in dic:
        temp=dic[x].copy()
        for y in temp:
            if int(y[2])<60 and int(y[3])<60 and int(y[4])<60:
                allfail.append(x)
                allfail.append(str(y[0]))
                allfail.append(str(y[1]))
    print("All Fail",allfail)

def SorceMostHigh(dic):
    temp=[]
    top=0
    prt=None
    hight=[]
    for x in dic:
        temp=dic[x].copy()
        for y in temp:
            if top<int(y[2])+int(y[3])+int(y[4]):
                top=int(y[2])+int(y[3])+int(y[4])
                prt=y
        hight.append(prt)
        top=0 
    print("Class {} students are : ".format("top Chinese source"))
    for x in dic:
        print("Class {} : ".format(x),end="")
        for y in hight:
            if y in dic[x]:
                print(y[1],end="")
        print()
ls=[]
dic={}
def GetData(data):    
    cprt=None
    for x in range(len(data)):
        temp=[]
        for y in list(data[x]):
            temp.append(y)
        ls.append(temp)
def DoX(x,temp):
    x.remove(x[0])
    temp.append(x)
    
def GetDic(ls):
    for x in ls:
        if x[0] not in dic.keys():
            temp=[]
            cprt=x[0]
            DoX(x,temp)
        else:
            temp=[]
            temp=dic[cprt].copy()
            DoX(x,temp)
        dic[cprt]=temp

GetData(GetDB())
GetDic(ls)
print(dic)
GetAllFail(dic)

MostStudent(dic,3)
SorceMostHigh(dic)
MostStudent(dic,1)
GetOverAvg(dic,GetAvg(dic))