class BankAcct:
    def __init__(self, name, account_number, initial_amount, interest_rate):
        self.name = name
        self.account_number = account_number
        self.amount = initial_amount
        self.interest_rate = interest_rate
    
    def adjust_interest_rate(self, new_interest_rate):
        """Adjusts the interest rate."""
        self.interest_rate = new_interest_rate
    
    def deposit(self, amount):
        """Deposits a specified amount into the account."""
        if amount > 0:
            self.amount += amount
        else:
            print("Deposit amount must be greater than zero.")
    
    def withdraw(self, amount):
        """Withdraws a specified amount from the account."""
        if 0 < amount <= self.amount:
            self.amount -= amount
        else:
            print("Withdrawal amount exceeds the available balance.")
    
    def get_balance(self):
        """Returns the current balance."""
        return self.amount
    
    def calculate_interest(self, days):
        """Calculates and returns the interest based on the number of days."""
        interest_amount = (self.amount * self.interest_rate / 100) * (days / 365)
        return interest_amount
    
    def __str__(self):
        """String representation of the object."""
        return f"Account Holder: {self.name}\nAccount Number: {self.account_number}\nBalance: ${self.amount:.2f}"
    

def test_bank_acct():
    # Create an instance of BankAcct
    acct = BankAcct("John Doe", "1234567890", 1000.00, 3.5)
    
    # Display initial account information
    print("Initial Account Information:")
    print(acct)
    print()
    
    # Adjust the interest rate
    acct.adjust_interest_rate(4.0)
    print("Adjusted Interest Rate to 4.0%")
    
    # Deposit some money
    acct.deposit(500.00)
    print("Deposited $500.00")
    print("Updated Account Information:")
    print(acct)
    print()
    
    # Withdraw some money
    acct.withdraw(200.00)
    print("Withdrew $200.00")
    print("Updated Account Information:")
    print(acct)
    print()
    
    # Calculate interest for 180 days
    days = 180
    interest_amount = acct.calculate_interest(days)
    print(f"Interest earned for {days} days: ${interest_amount:.2f}")
    print()


# Test the BankAcct class
if __name__ == "__main__":
    test_bank_acct()
