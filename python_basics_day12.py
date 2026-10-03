# Day 12 - Polymorphism (3 examples)

# Example 1: Method overriding (same method name, different behavior in child classes)
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

for animal in [Animal(), Dog(), Cat()]:
    animal.sound()

# Example 2: Polymorphism with functions (same function works for different objects)
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

def print_area(shape):
    print("Area:", shape.area())

print_area(Rectangle(5, 4))
print_area(Circle(3))

# Example 3: Built-in polymorphism (same operator/function, different behavior by type)
print(5 + 10)          # int addition
print("Hello " + "World")   # string concatenation
print([1, 2] + [3, 4])      # list concatenation

print(len("Monisha"))   # length of a string
print(len([1, 2, 3, 4]))   # length of a list
