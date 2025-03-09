# person class to manage bank accounts
from checking import Checking
from savings import Savings

class Person:
    def __init__(self, name, account_type):
        self.name = name
        if account_type == "Checking":
            self.account = Checking()
        elif account_type == "Savings":
            self.account = Savings()

    def interact(self):
        deposit_count = 0  # Track deposits for savings account profit calculation
        while True:
            action = input("Enter 'D' for Deposit, 'W' for Withdrawal, 'Q' to Quit: ").upper()
            if action == 'D':
                amount = float(input("Enter deposit amount: "))
                self.account.deposit(amount)
                deposit_count += 1
                if self.account.acct_type == "Savings" and deposit_count % 10 == 0:
                    self.account.profit()
            elif action == 'W':
                amount = float(input("Enter withdrawal amount: "))
                self.account.withdraw(amount)
                if self.account.current_balance < 0:
                    self.account.over_draft += 200
                    print("Warning: Overdraft limit increased by 200. New overdraft limit:", self.account.over_draft)
            elif action == 'Q':
                print("Exiting...")
                break
            else:
                print("Invalid action. Please try again.")