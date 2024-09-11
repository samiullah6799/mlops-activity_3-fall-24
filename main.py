

class Account:
    def __init__(self, balance):
        self.balance = balance

    def getAmount(self):
        return self.balance
    
    def deposit(self, balance):
        self.balance = self.balance + balance

    def withDraw(self, balance):
        self.balance = self.balance - balance