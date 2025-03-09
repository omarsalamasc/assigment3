# person class to manage bank accounts
from checking import Checking
from savings import Savings

class Person:
    def __init__(self, name, account_type):
        self.name = name
        # create appropriate account type based on input
        if account_type == "Checking":
            self.account = Checking()
        elif account_type == "Savings":
            self.account = Savings()

    # method to handle all banking interactions
    def interact(self):
        deposit_count = 0  # track deposits for savings account profit calculation
        while True:
            print("\nCurrent Balance: $" + str(self.account.current_balance))
            print("Account Type: " + self.account.acct_type)
            action = input("Enter 'D' for Deposit, 'W' for Withdrawal, 'Q' to Quit: ").upper()
            
            if action == 'D':
                amount = float(input("Enter deposit amount: "))
                self.account.deposit(amount)
                deposit_count += 1
                # check if savings account needs to add profit
                if self.account.acct_type == "Savings" and deposit_count % 10 == 0:
                    self.account.profit()
            
            elif action == 'W':
                amount = float(input("Enter withdrawal amount: "))
                self.account.withdraw(amount)
                # check for overdraft
                if self.account.current_balance < 0:
                    self.account.over_draft += 200
                    print("Warning: Overdraft limit increased by 200. New overdraft limit: " + str(self.account.over_draft))
            
            elif action == 'Q':
                print("Thank you for banking with us, " + self.name)
                break
            
            else:
                print("Invalid action. Please try again.")

# example of how to run the program
if __name__ == "__main__":
    name = input("Enter your name: ")
    account_type = input("Enter account type (Checking/Savings): ")
    customer = Person(name, account_type)
    customer.interact() 