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
        self.i=0
        self.time=0
    def Join(self,player):
        self.member.append(player)
    @abc.abstractmethod
    def StartGame():
        return Notimplemented

class DiceGame(Game):
    def StartData(self):
        for x in self.member:
            data_temp=[]
            for _ in range(6):
                data_temp.append(random.randint(1,6))
            x.data=tuple(data_temp)
    def StartGame(self):
        stander=[]
        while True:
            print(len(self.member),self.member[self.i].Name(),stander,self.i)
            inpu=input("input your chooce:").split(",")
            if self.ReviewInput(inpu)==True:
                if inpu[0]==self.member[self.i].Name():
                    if self.time==0:
                        stander=[int(inpu[1]),int(inpu[2])]
                        self.time=1
                        self.i=self.i+1
                    else:
                        if(int(inpu[1])<stander[0]) or (int(inpu[2])<stander[1]) or (int(inpu[1])==stander[0] and int(inpu[2])==stander[1]) :
                            print("error now is ",stander)
                        elif int(inpu[1])>6 or int(inpu[2])>6:
                            print("your input outoff range")
                        else:
                            stander[0]=int(inpu[1])
                            stander[1]=int(inpu[2])
                            if self.i==len(self.member)-1:
                                self.i=0
                            else:
                                self.i=self.i+1
                elif inpu[0]=="抓":
                    self.WinOrLose(i)
                else :
                    print("error input please try again")
                if stander[0]>=6 and stander[1]>=6:
                    inpu=input("input:").split(",")
                    self.WinOrLose(i)
                    break
            else: 
                print(self.ReviewInput(inpu))
    def WinOrLose(self,i):
        print("in winorlose")
    def ReviewInput(self,inpu):
        if len(inpu)!=1 and len(inpu) != 3:
            return "your input was error \nplease try again"
        elif inpu=="抓":
            if self.time == 0:
                return"you have input value\nplease try again"
        elif inpu[1].isdigit()==False or inpu[2].isdigit()==False:
            return "you have invade input\nplease try again"
                
        else:
            return True
Dice=DiceGame()
while(True): 
    inpu=input("input:").split("/")
    if inpu[0] == "start":
        break
    elif inpu[1] == "join":
        inpu[0]=Player(inpu[0])
        Dice.member.append(inpu[0])
    else:
        print("error inpu")
Dice.StartData()
Dice.StartGame()