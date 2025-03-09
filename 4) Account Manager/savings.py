# import account class from account.py file
from account import Account

class Savings(Account):
    def __init__(self):
        Account.__init__(self, "Savings")
        self.over_draft = 1200  # Overdraft limit for savings accounts

    def profit(self):
        profit_amount = self.current_balance * 0.15
        self.current_balance += profit_amount
        print("Profit calculated and added:", profit_amount, "Current balance:", self.current_balance)