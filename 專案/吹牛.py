import abc
import random

class Player():
    def __init__(self,x):
        self.data=()
        self.name=x
    def Name(self):
        return self.name

class Game():
    def __init__(self):
        self.member=[]
        self.temp=[]
    def Join(self,player):
        self.member.append(player)
    @abc.abstractmethod
    def StartGame():
        return Notimplemented

class DiceGame(Game):
    def StartData(self):
        for x in self.temp:
            x=Player(x)
            data_temp=[]
            for _ in range(6):
                data_temp.append(random.randint(1,6))
            x.data=tuple(data_temp)
            self.member.append(x)
    def StartGame(self):
        i=0
        stander=[1,1]
        while True:
            print(len(self.member),self.member[i].Name(),stander)
            inpu=input("input your choice:").split(",")
            
            if inpu[0]==self.member[i].Name():
                if (int(inpu[1])<stander[0]) or (int(inpu[2])<stander[1]) or (int(inpu[1])==stander[0] and int(inpu[2])==stander[1]) :
                    print("error now is ",stander)
                elif int(inpu[1])>6 or int(inpu[2])>6:
                    print("your input outoff range")
                else:
                    stander[0]=int(inpu[1])
                    stander[1]=int(inpu[2])
                    if i==len(self.member)-1:
                        i=0
                    else:
                        i=i+1
            
            elif inpu[0]=="抓":
                self.WinOrLose(i)
            else :
                print("error input please try again")
            if stander[0]>=6 and stander[1]>=6:
                inpu=input("input:").split(",")
                self.WinOrLose(i)
                print("look")
                break
            print(len(self.member),self.member[i].Name())
    def WinOrLose(self,i):
        print("in winorlose")
Dice=DiceGame()
i=0
while(True): 
    inpu=input("input:")
    if inpu == "start":
        break
    elif inpu == "join":
        Dice.temp.append(str(i))
        i=i+1
    else:
        print("error inpu")
Dice.StartData()
Dice.StartGame()