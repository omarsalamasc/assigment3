# import Account class object from account.py
from account import Account

class Checking(Account):
    def __init__(self):
        Account.__init__(self, "Checking")
        self.over_draft = 1000  # Overdraft limit for checking accounts