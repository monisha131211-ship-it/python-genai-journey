# Day 10 - Access Modifiers and Encapsulation (3 examples each)

# ================= ACCESS MODIFIERS (3 examples) =================

# Example 1: Public member (accessible from anywhere)
class Student:
    def __init__(self, name):
        self.name = name   # public

s = Student("Monisha")
print(s.name)

# Example 2: Protected member (convention: single underscore)
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary   # protected

class Manager(Employee):
    def show_salary(self):
        print(f"{self.name}'s salary: {self._salary}")

m = Manager("Krishna", 50000)
m.show_salary()

# Example 3: Private member (double underscore)
class Account:
    def __init__(self, balance):
        self.__balance = balance   # private

    def get_balance(self):
        return self.__balance

acc = Account(10000)
print(acc.get_balance())
