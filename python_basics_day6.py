# Day 6 - Python OOP: Inheritance, Multiple Inheritance, Multilevel Inheritance

# ================= INHERITANCE (3 examples) =================

# Example 1: Basic inheritance
class Animal:
    def sound(self):
        print("This animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.sound()
d.bark()

# Example 2: Inheriting and using parent's __init__
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

e = Employee("Monisha", 30000)
e.display()

# Example 3: Overriding a parent method
class Vehicle:
    def start(self):
        print("Vehicle starting")

class Car(Vehicle):
    def start(self):
        print("Car starting with key")

c = Car()
c.start()


# ================= MULTIPLE INHERITANCE (3 examples) =================

# Example 1: Two parent classes
class Father:
    def skills(self):
        print("Father: Business skills")

class Mother:
    def talent(self):
        print("Mother: Painting talent")

class Child(Father, Mother):
    pass

ch = Child()
ch.skills()
ch.talent()

# Example 2: Multiple parents with their own methods
class Flyer:
    def fly(self):
        print("Can fly")

class Swimmer:
    def swim(self):
        print("Can swim")

class Duck(Flyer, Swimmer):
    pass

duck = Duck()
duck.fly()
duck.swim()

# Example 3: Multiple inheritance with same method name (MRO - left to right)
class A:
    def show(self):
        print("Class A")

class B:
    def show(self):
        print("Class B")

class C(A, B):
    pass

obj = C()
obj.show()   # takes A's method first (left to right order)


# ================= MULTILEVEL INHERITANCE (3 examples) =================

# Example 1: Grandparent -> Parent -> Child
class Grandparent:
    def house(self):
        print("Has a house")

class Parent(Grandparent):
    def car(self):
        print("Has a car")

class Kid(Parent):
    def bike(self):
        print("Has a bike")

k = Kid()
k.house()
k.car()
k.bike()

# Example 2: Employee hierarchy
class Company:
    def name(self):
        print("Company: TechSoft")

class Department(Company):
    def dept(self):
        print("Department: IT")

class Employee2(Department):
    def role(self):
        print("Role: Software Engineer")

emp = Employee2()
emp.name()
emp.dept()
emp.role()

# Example 3: Shape hierarchy
class Shape:
    def info(self):
        print("This is a shape")

class Polygon(Shape):
    def sides(self):
        print("A polygon has many sides")

class Triangle(Polygon):
    def type_(self):
        print("A triangle has 3 sides")

t = Triangle()
t.info()
t.sides()
t.type_()
