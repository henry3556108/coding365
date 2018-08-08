import abc

class OldInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def click(self):
        return NotImplemented
    @abc.abstractmethod
    def dbclick(self):
        return NotImplemented
    @abc.abstractmethod
    def rightclick(self):
        return NotImplemented

class OldApi(OldInterface):
    def click(self):
        print("click")
    def dbclick(self):
        print("dbclick")
    def rightclick(self):
        print("rightclick")

class NewInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def mouseclick(self):
        return NotImplemented
    @abc.abstractmethod
    def mousedbclick(self):
        return NotImplemented
    @abc.abstractmethod
    def mouserightclick(self):
        return NotImplemented
        
class adapter(NewInterface):
    def __init__(self,old):
        self.old=old
    def mouseclick(self):
        old.click()
    def mousedbclick(self):
        old.dbclick()
    def mouserightclick(self):
        self.old.rightclick()

old=OldApi()
new=adapter(old)


 
def main():
    old.click()
    old.dbclick()
    old.rightclick()
    new.mouseclick()
    new.mousedbclick()
    new.mouserightclick()

if __name__=='__main__':
    main()