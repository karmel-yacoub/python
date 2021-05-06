class BankAccount:
	def __init__(self, int_rate, balance): # don't forget to add some default values for these parameters!
		# your code here! (remember, this is where we specify the attributes for our class)
                # don't worry about user info here; we'll involve the User class soon
        self.int_rate=0
        self.balance=o
	def deposit(self, amount):
		self.balance +=amount
	def withdraw(self, amount):
		self.balance -=amount
	def display_account_info(self):
		print("Balance: $100",self.balance)
	def yield_interest(self):
		