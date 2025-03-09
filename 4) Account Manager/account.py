# account class to manage banking transactions
class Account:
    def __init__(self, acct_type):
        self.acct_type = acct_type
        self.min_balance = 500
        self.current_balance = 0
        self.over_draft = 0  # Overdraft will be set in child classes

    def withdraw(self, amount):
        if self.current_balance - amount < -self.over_draft:
            print("Cannot withdraw: Overdraft limit exceeded.")
        else:
            self.current_balance -= amount
            print("Withdrawal of", amount, "successful. Current balance:", self.current_balance)

    def deposit(self, amount):
        self.current_balance += amount
        print("Deposit of", amount, "successful. Current balance:", self.current_balance)

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
