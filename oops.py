from abc import ABC,abstractmethod
class BankAccount:
    def __init__(self,amount,holder):
        self.amount=amount 
        self.holder=holder   
    def deposit(self,x):
        self.amount+=x
    def withdraw(self,x):
        self.amount-=x

class currentAccount(BankAccount): #Inheritance
    def __init__(self, amount, owner,overdraft):
        super().__init__(amount, owner)
        self.amount = amount
        self.overdraft=overdraft
    
    def withdraw(self, x):                
        if x <= self.amount+self.overdraft:
            self.amount-=x

class SavingAccount(BankAccount):
    def __init__(self, amount, holder):
        super().__init__(amount, holder)
        self.amount = amount
    
    def interest_rate(self):
        interest = self.amount * 0.025 
        self.amount+=interest

b1 = BankAccount(25000,"Krishn")
c1 = currentAccount(25000,"Krishn",2000)
s1 = SavingAccount(25000,"Krishn")
print(f"Account holder's name: {b1.holder} ")
print(f"Current balance is: {b1.amount}")



        
        