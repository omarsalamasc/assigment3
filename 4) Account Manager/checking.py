# checking account class that inherits from base account
from account import Account

class Checking(Account):
    def __init__(self):
        super().__init__()
        self.acct_type = "Checking"
        self.over_draft = 1000  # starting overdraft limit for checking 