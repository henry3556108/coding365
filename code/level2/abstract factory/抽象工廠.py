import abc

class Fruit(abc.ABC):
    def __init__(self,name):
        self.name=name
    @abc.abstractmethod
    def plant():
        return Notimplement
    @abc.abstractmethod
    def grow():
        return Notimplement
    @abc.abstractmethod
    def harvest():
        return Notimplement
        
class Apple(Fruit):
    def __init__(self,age):
        self.treeage=age
        super(Apple,self).__init__('Apple')
    def plant(self):
        print("Planting Apple")
        print("your Appletree age is ",self.treeage)
    def grow(self):
        print('growing apple')
    def harvest(self):
        print('you got apple')
        
class Grape(Fruit):
    def __init__(self,seed):
        self.seed=seed
        super(Grape,self).__init__('Grape')
    def plant(self):
        print("Planting Grape")
        if self.seed==True:
            print("your Grape has seed")
        elif self.seed==False:
            print("your Grape hasn't seed")
        
    def grow(self):
        print('growing Grape')
    def harvest(self):
        print('you got Grape')
        
class Strawberry(Fruit):
    def __init__(self):
        super(Strawberry,self).__init__('Strawberry')
    def plant(self):
        print("Planting Strawberry")
    def grow(self):
        print('growing Strawberry')
    def harvest(self):
        print('you got Strawberry')
 
class Veggie(abc.ABC):

    def __init__(self, name):
        self.name=name
    @abc.abstractmethod
    def plant(self):
        return NotImplemented
    @abc.abstractmethod
    def grow(self):
        return NotImplemented
    @abc.abstractmethod
    def deworm(self):
        return NotImplemented
    @abc.abstractmethod
    def harvest(self):
        return NotImplemented

class Cabbage(Veggie):
    def __init__(self):
        super(Cabbage, self).__init__('Cabbage')
    def plant(self):
        print(self.name, ' planting!!!')
    def grow(self):
        print(self.name, ' growing!!!')
    def deworm(self):
        print(self.name, ' deworming!!!')
    def harvest(self):
        print(self.name, ' harvesting!!!')

class Lettuce(Veggie):
    def __init__(self):
        super(Lettuce, self).__init__('Lettuce')
    def plant(self):
        print(self.name, ' planting!!!')
    def grow(self):
        print(self.name, ' growing!!!')
    def deworm(self):
        print(self.name, ' deworming!!!')
    def harvest(self):
        print(self.name, ' harvesting!!!')
        
class Cabbage(Veggie):
    def __init__(self):
        super(Cabbage, self).__init__('Cabbage')
    def plant(self):
        print(self.name, ' planting!!!')
    def grow(self):
        print(self.name, ' growing!!!')
    def deworm(self):
        print(self.name, ' deworming!!!')
    def harvest(self):
        print(self.name, ' harvesting!!!')

class Lettuce(Veggie):
    def __init__(self):
        super(Lettuce, self).__init__('Lettuce')
    def plant(self):
        print(self.name, ' planting!!!')
    def grow(self):
        print(self.name, ' growing!!!')
    def deworm(self):
        print(self.name, ' deworming!!!')
    def harvest(self):
        print(self.name, ' harvesting!!!')
        
class Gardener(abc.ABC):
    def __init__(self,type):
        self.type=type
        self.creatfruitls=[]
        self.creatvegetls=[]
    @abc.abstractmethod
    def creatfruit():
        return NotImplemented
    
    @abc.abstractmethod
    def creatveget():
        return NotImplemented
        
    @abc.abstractmethod
    def printall():
        return NotImplemented
        
class NorthGardener(Gardener):
    def __init__(self):
        super(NorthGardener, self).__init__("North")
    def creatfruit(self, name, seed = None, treeAge = None):
        if name == 'Grape':
            self.creatfruitls.append(Grape(seed))
        elif name == 'Strawberry':
            self.creatfruitls.append(Strawberry())
        elif name == 'Apple':
            self.creatfruitls.append(Apple(treeAge))
        else:
            print('ERROR')
    def creatveget(self, name):
        if name == 'Cabbage':
            self.creatvegetls.append(Cabbage())
        elif name == 'Lettuce':
            self.creatvegetls.append(Lettuce())
        else:
            print('ERROR')
        
    def printall(self):
        for i in self.creatfruitls:
            i.plant()
            i.grow()
            i.harvest()
        for i in self.creatvegetls:
            i.plant()
            i.grow()
            i.deworm()
            i.harvest()

class TropicalGardener(Gardener):
    def __init__(self):
        super(TropicalGardener, self).__init__("Tropical")
    def creatfruit(self, name, seed = None, treeAge = None):
        if name == 'Grape':
            self.creatfruitls.append(Grape(seed))
        elif name == 'Strawberry':
            self.creatfruitls.append(Strawberry())
        elif name == 'Apple':
            self.creatfruitls.append(Apple(treeAge))
        else:
            print('ERROR')
    def creatveget(self, name):
        if name == 'Cabbage':
            self.creatvegetls.append(Cabbage())
        elif name == 'Lettuce':
            self.creatvegetls.append(Lettuce())
        else:
            print('ERROR')
    def printall(self):
        for i in self.creatfruitls:
            i.plant()
            i.grow()
            i.harvest()
        for i in self.creatveget:
            i.plant()
            i.grow()
            i.deworm()
            i.harvest()

a = NorthGardener()
a.creatfruit('Grape', False)
a.creatveget('Lettuce')
a.creatfruit('Apple', None, '5')
a.printall()

b = NorthGardener()
b.creatfruit('Grape', True)
b.creatveget('Lettuce')
b.creatfruit('Apple', None,'6')
b.printall()