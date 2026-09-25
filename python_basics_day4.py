# Day 4 - Python Functions (Type of arguments, Return function, Local and Global)

# 1. Type of arguments
# Default argument
def greet(name, msg="Good morning"):
    print(f"{msg}, {name}")

greet("Monisha")
greet("Monisha", "Good evening")

# Variable-length argument (*args)
def add(*numbers):
    print(sum(numbers))

add(2, 3, 4)

# 2. Return function
def square(n):
    return n * n

result = square(5)
print(result)

# 3. Local and Global variables
x = 10   # global variable

def show():
    x = 5   # local variable
    print("Inside function:", x)

show()
print("Outside function:", x)
