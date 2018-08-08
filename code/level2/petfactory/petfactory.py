class Pet:
    _name=None
    def eat(self):
        print("eat")
    def walk(self):
        print("walk")
    def sleep(self):
        print(self._name,end='')
        print(" sleep")
        
class Dog(Pet):
    def __init__(self):
        self._name='Dog'
    def eat(self):
        print("吃得很醜")
    def bark(self):
        print("旺旺旺")

class Cat(Pet):
    def __init__(self):
        self._name='Cat'
    def eat(self):
        print("吃得很美")
        
class Bird(Pet):
    def __init__(self):
        self._name='Bird'
        
class CatDog(Cat,Dog):
    def __init__(self,name):
        self.name=name
        
class PetFactory:
    def CreatPet(self,name):
        if name=='Dog':
            return Dog()
        
        if name=='Cat':
            return Cat()
        
        if name=='Bird':
            return Bird()
freak=CatDog("dacy")
freak.eat()
