from abc import ABC, abstractmethod 
class Bank(ABC):  
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate
    
    def bank_info(self):
        print(f"Welcome to {self.name} Bank")

    @abstractmethod
    def interest(self):
        pass

class ICICI(Bank):
    def __init__(self):
        super().__init__("ICICI", 10) 
    
    def interest(self):
        print(f"Interest Rate of {self.name} Bank: {self.rate}%")

class SBI(Bank):
    def __init__(self):
        super().__init__("SBI", 7)  
    
    def interest(self):
        print(f"Interest Rate of {self.name} Bank: {self.rate}%")

icici_bank = ICICI()
sbi_bank = SBI()
icici_bank.interest()
sbi_bank.interest()
