inpu=input("").split(" ")
value=0
key=0
cards={}
card=[]
nls=[]
style=''
straight=0
newls=[]
def judgestraight(ls,dict,kind):
    if (int(ls[2])+int(ls[1])+int(ls[0])+int(ls[3])+int(ls[4]))/5==int(ls[2]):
        kind='6'
    elif ls[4]==13 and ls[0]==1 and ls[1]==2 and ls[2]==3 and ls[3]==4:
        kind='6'
    if kind=='6':
        if dict[str(ls[0])]==dict[str(ls[1])]==dict[str(ls[2])]==dict[str(ls[3])]==dict[str(ls[4])]:
            kind='7'
    return kind
def judge(ls,dict):
    kind='0'
    newls=ls.copy()
    for x in range(len(newls)):
        newls[x]=int(ls[x])
    newls.sort()
    if len(ls)==5:
        kind=judgestraight(newls,dict,kind)
    for x in ls:
        nls=dict[x].copy()
        if kind=='0' and len(nls)==2:
            kind='1'
        elif kind=='1'and len(nls)==2:
            kind='2'
        elif kind=='0'and len(nls)==3:
            kind='3'
        elif kind=='1'and len(nls)==3:
            kind='4'
        elif kind=='3'and len(nls)==2:
            kind='4'
        elif kind=='0'and len(nls)==4:
            kind='5'
        else : pass
    return kind
for x in inpu:
    ls=[]
    key=str(int(int(x)/10))
    value=str(int(x)%10)
    if cards.get(key,None)==None:
        ls.append(value)
        cards[key]=ls
        card.append(key)
    else:
        ls=cards[key].copy()
        ls.append(value)
        cards[key]=ls
style=judge(card,cards)
print(style)