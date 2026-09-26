# Day 5 - Python OOP Basics (Debugging, OOP, self & __init__, Class Method)

# 1. Debugging in Python
# A simple bug example and how to find it
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: cannot divide by zero")
        return None

print(divide(10, 2))
print(divide(10, 0))

# 2. OOP - creating a simple class
class Student:
    college = "Ethiraj College"   # class attribute (same for all objects)

    # 3. self and __init__()
    def __init__(self, name, age):
        self.name = name   # instance attribute (unique per object)
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, College: {self.college}")

# Creating objects
s1 = Student("Monisha", 21)
s2 = Student("Krishna", 22)

s1.display()
s2.display()

# 4. Class method (works on the class itself, not one object)
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print("Total objects created:", cls.count)

c1 = Counter()
c2 = Counter()
c3 = Counter()
Counter.show_count()
