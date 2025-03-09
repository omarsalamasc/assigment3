# savings account class that inherits from base account
from account import Account

class Savings(Account):
    def __init__(self):
        super().__init__()
        self.acct_type = "Savings"
        self.over_draft = 500  # starting overdraft limit for savings
        self.interest_rate = 0.05  # 5% interest rate
    
    # profit method to add interest to savings account
    def profit(self):
        interest = self.current_balance * self.interest_rate
        self.current_balance += interest
        print("Interest added: $" + str(interest))
        print("New Balance: $" + str(self.current_balance)) 