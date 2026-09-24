# Day 3 - Python Basics (if-else, Nested if, Multiple if, List, Set, Tuple, Dict)

# 1. if-else
height = int(input("Enter height in feet: "))
if height > 3:
    print("Buy Token")
else:
    print("No token required")

# 2. if-else (even/odd)
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")

# 3. Nested if-else
age = int(input("Enter your age: "))
if age > 0:
    if age >= 18:
        print("Adult")
    else:
        print("Minor")
else:
    print("Invalid age")

# 4. Multiple if (grading)
marks = 75
if marks >= 90:
    print("Grade A")
if marks >= 60 and marks < 90:
    print("Grade B")
if marks < 60:
    print("Grade C")

# 5. List
fruits = ["apple", "banana", "cherry"]
print(fruits)
fruits.append("mango")
print(fruits)

# 6. Set
colors = {"red", "green", "blue", "red"}
print(colors)

# 7. Tuple
coordinates = (10, 20)
print(coordinates)

# 8. Dictionary
student = {"name": "Monisha", "age": 21}
print(student)
print(student["name"])
