# account class to manage banking transactions
class Account:
    # initialize account with type and default values
    def __init__(self, acct_type):
        self.acct_type = acct_type
        self.min_balance = 500
        self.current_balance = 0

    # withdraw money and check for overdraft
    def withdraw(self, amount):
        self.current_balance -= amount
        # check if balance goes negative
        if self.current_balance < 0:
            self.current_balance -= 200
            print("Warning: Overdraft limit exceeded.")
        else:
            print(f"Withdrawal of {amount} successful. Current balance: {self.current_balance}")

    # deposit money into account
    def deposit(self, amount):
        self.current_balance += amount
        print(f"Deposit of {amount} successful. Current balance: {self.current_balance}")

# Test the Account class
if __name__ == "__main__":
    # Create a new savings account
    savings = Account("savings")
    
    # Test deposit functionality
    savings.deposit(1000)
    
    # Test withdrawal functionality
    savings.withdraw(300)
    
    # Test overdraft scenario
    savings.withdraw(800)
