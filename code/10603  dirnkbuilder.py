import abc

class Builder:
    def __init__(self, name):
        self.name = name
    @abc.abstractmethod
    def brew(self):
        return NotImplemented
    @abc.abstractmethod
    def flavor(self):
        return NotImplemented
    @abc.abstractmethod
    def mix(self):
        return NotImplemented

    def howToMake(self):
        print('開始製作{}'.format(self.name))
        print('第一步: ',end = '')
        self.brew()
        print('第二步: ',end = '')
        self.flavor()
        print('第三步: ',end = '')
        self.mix()
class MilkTeaBuilder(Builder):
    def __init__(self):
        super(MilkTeaBuilder, self).__init__('奶茶')
    def brew(self):
        print("泡紅茶")
    def flavor(self):
        print("加入鮮奶")
    def mix(self):
        print("撒上少許巧克力粉")
        
class CoffeeBuilder(Builder):
    def __init__(self):
        super(CoffeeBuilder, self).__init__('咖啡')
    def brew(self):
        print("研磨")
    def flavor(self):
        print("加入奶精")
    def mix(self):
        print("撒上少許肉桂粉")
        
class Director:
    def __init__(self, builder):
        self.build = builder
    def show(self):
        self.build.howToMake()
        
milktea=MilkTeaBuilder()
D=Director(milktea)
D.show()