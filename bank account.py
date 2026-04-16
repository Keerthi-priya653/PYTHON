class bankaccount:
    def __init__(self,name, balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdraw(self,amount):
        self.balance=self.balance-amount
    def display(self): 
        print(self.name,"balance is:",self.balance)
ba=bankaccount( "CSE",10000)
ba.deposit(1000)
ba.withdraw(500)
ba.display()
        
