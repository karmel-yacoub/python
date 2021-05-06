class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate=int_rate
        self.balance=balance
    def deposit(self, amount):
        self.balance +=amount
        return self
    def withdraw(self, amount):
        self.balance -=amount
        return self
    def display_account_info(self):
        print("Balance:",self.balance)
    def yield_interest(self):
        self.balance = self.balance+self.balance*self.int_rate
        return self
karmel= BankAccount(0.5,1000)
karmel.display_account_info()
print(karmel.yield_interest())
karmel.deposit(200).deposit(400).deposit(300).withdraw(200)

hadeel= BankAccount(0.3,2000)
hadeel.display_account_info()
print(hadeel.yield_interest())
hadeel.deposit(50).deposit(200).withdraw(100).withdraw(50).withdraw(20).withdraw(30).yield_interest().display_account_info()




