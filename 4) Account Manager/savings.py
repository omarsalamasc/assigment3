# import account class from account.py file
from account import Account

class Savings(Account):
    def __init__(self):
        # call parent class constructor with account type "savings"
        super().__init__("Savings") 
        # set overdraft limit specific to savings accounts
        self.over_draft = 1200  # overdraft limit for savings account

    def profit(self):
        # calculate 15% profit on current balance
        profit_amount = self.current_balance * 0.15
        # add calculated profit to current balance
        self.current_balance += profit_amount
        # display profit added and new balance
        print(f"Profit calculated and added: {profit_amount}. Current balance: {self.current_balance}")