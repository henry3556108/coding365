import abc
    

class Part(abc.ABC):
    price = 0
    def __init__(self,Price):
        self.price=Price
    @abc.abstractmethod
    def GetPrice(self):
        return NotImplemented
                
class CPU(Part):
    def __init__(self):
        super(CPU,self).__init__(2000)
    def GetPrice(self):
        return self.price

class RAM(Part):
    def __init__(self):
        super(RAM,self).__init__(1200)
    def GetPrice(self):
        return self.price
    

class HHD(Part):
    def __init__(self):
        super(HHD,self).__init__(3000)
    def GetPrice(self):
        return self.price
    
class Register():
    __register = None
    @classmethod  
    def getSingleton(cls):  
        if not isinstance(cls.__register,cls):  
            cls.__register = cls()   
        else:print("error")
        return cls.__register
    def summ(self,ls):
        sum=0
        for x in ls:
            sum+=x.GetPrice()    
        return sum
    
def main():
    register1=Register.getSingleton()
    register2=Register.getSingleton()
    if id(register2)==id(register1):
        register2=None
    i7=CPU()
    HD=HHD()
    DDR3=RAM()
    ls=[i7,HD,DDR3]
    sum=register1.summ(ls)
    print(sum)
    
if __name__=='__main__':
    main()
    
    