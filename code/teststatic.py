class Singleton:  
    __singleton = None  
    @classmethod  
    def getSingleton(Singleton):  
        if not isinstance(Singleton.__singleton,Singleton):  
            Singleton.__singleton = Singleton()  
        return Singleton.__singleton  

class Test(Singleton) :  
    def test(self):  
        return id(self)  

class Test1(Test):  
    def test1(self):  
        print(self.__class__,id(self),'Test1')
        
class Test2(Singleton):  
    def test2(self):  
        print (self.__class__,id(self),'Test2')
  
if __name__== '__main__' :  
    t1 = Test.getSingleton()  
    t2 = Test.getSingleton()  
    if t1.test() == t2.test():
        t2=None
      