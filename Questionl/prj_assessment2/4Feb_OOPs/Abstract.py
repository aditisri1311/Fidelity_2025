from abc import *
class Printer(ABC):
    @abstractmethod
    def printing(self, text):
        pass #Abstract method, must be overridden
    
class HP(Printer):
    def printing(self, text):
        return f"HP Printing:{text}"
       
obj = HP()
print(obj.printing("Hello, World!"))