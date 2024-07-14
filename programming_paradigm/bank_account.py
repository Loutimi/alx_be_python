class BankAccount:
    def __init__(self, account_balance, initial_balance = 0):
        self.account_balance = account_balance
        self.initial_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount
        return 

    def withdraw(self, amount):
        if self.account_balance > amount:
            self.account_balance -= amount
            return True
        else:
            self.account_balance
            return False
        
    def display_balance(self):
        return f"Current Balance: ${amount}"

