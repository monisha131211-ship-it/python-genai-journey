# ================= CLASS (3 examples) =================

# Example 1: Simple class with attributes and method
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f"'{self.title}' by {self.author}")

b = Book("Atomic Habits", "James Clear")
b.display()

# Example 2: Class with a class variable shared by all objects
class Bank:
    bank_name = "State Bank"

    def __init__(self, balance):
        self.balance = balance

    def show_balance(self):
        print(f"{Bank.bank_name} - Balance: {self.balance}")

acc1 = Bank(5000)
acc2 = Bank(12000)
acc1.show_balance()
acc2.show_balance()

# Example 3: Class with multiple methods
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

calc = Calculator()
print("Sum:", calc.add(10, 5))
print("Difference:", calc.subtract(10, 5))
