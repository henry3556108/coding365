ls = []
ls2=['Name:','Id:','Total:','Average:']
for x in range(5):
    inpu=input("")
    ls.append(inpu)
sum=int(ls[2])+int(ls[3])+int(ls[4])

average=sum/3
average=int(average)
for x in range(3):
    ls.pop()
ls.append(str(sum))
ls.append(str(average))
for x in range(4):
    print(ls2[x]+ls[x])