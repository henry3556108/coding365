import abc

class Part(abc.ABC):
    price = 0
    def __init__(self,Price):
        self.price=Price
    def GetPrice(self):
        return self.price
        
class CPU(Part):
    def __init__(self):
        super(CPU,self).__init__(2000)
    

class RAM(Part):
    def __init__(self):
        super(RAM,self).__init__(1200)
    

class HHD(Part):
    def __init__(self):
        super(HHD,self).__init__(3000)
    
class Register():
    sum=0
    i7=CPU()
    HHD=HHD()
    DDR3=RAM()
    ls=[i7,HHD,DDR3]
    for x in ls:
        sum+=x.GetPrice()    
    
    
def main():
    register1=Register()
    print(register1.sum)
    
    
if __name__=='__main__':
    main()
    
    