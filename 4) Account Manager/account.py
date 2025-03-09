# base account class to manage basic banking functions
class Account:
    def __init__(self):
        self.current_balance = 0
        self.over_draft = 0
        self.acct_type = ""
    
    # deposit method to add money to account
    def deposit(self, amount):
        if amount > 0:
            self.current_balance += amount
            print("Deposited: $" + str(amount))
            print("Current Balance: $" + str(self.current_balance))
        else:
            print("Invalid deposit amount")
    
    # withdraw method to take money from account
    def withdraw(self, amount):
        if amount > 0:
            if self.current_balance - amount >= -self.over_draft:
                self.current_balance -= amount
                print("Withdrawn: $" + str(amount))
                print("Current Balance: $" + str(self.current_balance))
            else:
                print("Insufficient funds - exceeds overdraft limit")
        else:
            print("Invalid withdrawal amount") 