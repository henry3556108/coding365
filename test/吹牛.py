import abc
import random

class Player():
    def __init__(self,x):
        self.data=()
        self.name=x
    def Name(self):
        return self.name
    def Data(self):
        return self.data

class Game():
    def __init__(self):
        self.member=[]
        self.i=0
        self.time=0
    def Join(self,player):
        self.member.append(player)
    def NowPlayer():
        return self.member[self.i]
    @abc.abstractmethod
    def StartGame():
        return Notimplemented
    def Join(self,name):
        self.member.append(name)
class DiceGame(Game):




def InitGame():
    while True:
        temp=[] 
        inpu=input("input:").split("/")
        if inpu[0] == "start":
            return temp
        elif inpu[1] == "join":
            temp.append(inpu[0])
        else:
            print("error inpu")

if __name__=='__main__':
    member=[]
    checkmember=InitGame()
    