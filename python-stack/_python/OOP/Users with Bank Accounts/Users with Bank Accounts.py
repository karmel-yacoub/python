class user:

    def __init__(self,name):
        self.name =name
        self.account_balance=BankAccount(name=user,int_rate=0.02,account_balance=0)
    def deposit(self,amount):
        self.account_balance.deposit(amount)		
        return self		
    def withdrawal(self,amount):
        self.account_balance.withdrawl(amount)
        return self
    


class BankAccount:
    def __init__(self, int_rate, account_balance):
        self.int_rate=int_rate
        self.account_balance=account_balance
    def deposit(self, amount):
        self.account_balance +=amount
        return self
    def withdraw(self, amount):
        self.account_balance -=amount
        return self
    def display_account_info(self):
       return self.account_balance
    def yield_interest(self):
        if self.account_balance>0:
            self.account_balance = self.account_balance+self.account_balance*self.int_rate
            return self
karmel=user('karmel')
karmel.deposit(200).deposit(400).deposit(300).withdrawl(200)
hadeel=user('hadeel')
hadeel.deposit(50).deposit(200).deposit(100).withdrawl(100)

print(karmel.account_balance.display_account_info())
print(hadeel.account_balance.display_account_info())