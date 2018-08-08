import abc

class FlyMoudle(abc.ABC):
    @abc.abstractmethod
    def fly():
        return NotImplemented
class NoFly(FlyMoudle):
    def fly(self):
        print("I can't fly")
class Fly(FlyMoudle):
    def fly(self):
        print("I do fly")

class QuackMoudle(abc.ABC):
    @abc.abstractmethod
    def quack():
        return NotImplemented
class Quack(QuackMoudle):
    def quack(self):
        print("呱呱")
class QuackStrange(QuackMoudle):
    def quack(self):
        print("吱吱")

class Duck():
    def __init__(self, name, flymove=None, quackmove=None):
        self.name=name
        self.flymove=flymove
        self.quackmove=quackmove
    
    def flyMove(self,flymove):
        self.flymove=flymove
        
    def quackMove(self,quackmove):
        self.quackmove=quackmove
        
    def fly(self):
        self.flymove.fly()
        
    def quack(self):
        self.quackmove.quack()
     
dacy=Duck("Dacy",NoFly(),Quack())
dacy.fly()
dacy.quack()