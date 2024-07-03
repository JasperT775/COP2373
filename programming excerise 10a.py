# Define the Money class with basic money operations
class Money:
    def __init__(self, amount=0.0):
        self.amount = amount
    
    def __add__(self, other):
        """Addition operator overload."""
        if isinstance(other, Money):
            return Money(self.amount + other.amount)
        else:
            raise TypeError("Unsupported operand type(s) for +: 'Money' and '{}'".format(type(other).__name__))
    
    def __sub__(self, other):
        """Subtraction operator overload."""
        if isinstance(other, Money):
            return Money(self.amount - other.amount)
        else:
            raise TypeError("Unsupported operand type(s) for -: 'Money' and '{}'".format(type(other).__name__))
    
    def __mul__(self, other):
        """Multiplication operator overload."""
        if isinstance(other, (int, float)):
            return Money(self.amount * other)
        else:
            raise TypeError("Unsupported operand type(s) for *: 'Money' and '{}'".format(type(other).__name__))
    
    def __str__(self):
        """String representation of Money object."""
        return f"${self.amount:.2f}"


# Test function to validate Money class operations
def test_money_operations():
    # Create instances of Money
    money1 = Money(100.0)
    money2 = Money(50.0)
    
    # Test addition
    result_add = money1 + money2
    print(f"Addition Result: {result_add}")  # Expected: $150.00
    
    # Test subtraction
    result_sub = money1 - money2
    print(f"Subtraction Result: {result_sub}")  # Expected: $50.00
    
    # Test multiplication
    scalar = 1.5
    result_mul = money1 * scalar
    print(f"Multiplication Result: {result_mul}")  # Expected: $150.00


# Run the test function if this file is executed directly
if __name__ == "__main__":
    test_money_operations()
