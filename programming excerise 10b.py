# Define a Money class with basic money operations
class Money:
    def __init__(self, amount=0.0):
        self.amount = amount
    
    def add(self, amount):
        """Adds the given amount to the current amount."""
        self.amount += amount
    
    def subtract(self, amount):
        """Subtracts the given amount from the current amount."""
        self.amount -= amount
    
    def get_amount(self):
        """Returns the current amount."""
        return self.amount


# Define BankAcct class inheriting from Money
class BankAcct(Money):
    def __init__(self, name, account_number, initial_amount=0.0, interest_rate=0.0):
        super().__init__(initial_amount)  # Initialize the amount using Money's constructor
        self.name = name
        self.account_number = account_number
        self.interest_rate = interest_rate
    
    def adjust_interest_rate(self, new_interest_rate):
        """Adjusts the interest rate."""
        self.interest_rate = new_interest_rate
    
    def calculate_interest(self, days):
        """Calculates and returns the interest based on the number of days."""
        interest_amount = (self.amount * self.interest_rate / 100) * (days / 365)
        return interest_amount
    
    def __str__(self):
        """String representation of the object."""
        return f"Account Holder: {self.name}\nAccount Number: {self.account_number}\nBalance: ${self.amount:.2f}"


# Test function to test the BankAcct class
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
    
    # Use add method to deposit money
    acct.add(500.00)
    print("Deposited $500.00")
    print("Updated Account Information:")
    print(acct)
    print()
    
    # Use subtract method to withdraw money
    acct.subtract(200.00)
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
