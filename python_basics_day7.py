# Day 7 - Python OOP: Hierarchical Inheritance and Hybrid Inheritance

# ================= HIERARCHICAL INHERITANCE (3 examples) =================
# One parent class -> many child classes

# Example 1: Animal -> Dog, Cat
class Animal:
    def eat(self):
        print("Animal eats food")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

d = Dog()
c = Cat()
d.eat()
d.bark()
c.eat()
c.meow()

# Example 2: Person -> Student, Teacher
class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)

class Student(Person):
    def role(self):
        print(self.name, "is a Student")

class Teacher(Person):
    def role(self):
        print(self.name, "is a Teacher")

s = Student("Monisha")
t = Teacher("Krishna")
s.show()
s.role()
t.show()
t.role()

# Example 3: Vehicle -> Car, Bike
class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    def wheels(self):
        print("Car has 4 wheels")

class Bike(Vehicle):
    def wheels(self):
        print("Bike has 2 wheels")

car = Car()
bike = Bike()
car.start()
car.wheels()
bike.start()
bike.wheels()


# ================= HYBRID INHERITANCE (3 examples) =================
# Combination of two or more types of inheritance

# Example 1: Hierarchical + Multiple
class A:
    def show_a(self):
        print("Class A")

class B(A):
    def show_b(self):
        print("Class B")

class C(A):
    def show_c(self):
        print("Class C")

class D(B, C):
    def show_d(self):
        print("Class D")

obj = D()
obj.show_a()
obj.show_b()
obj.show_c()
obj.show_d()

# Example 2: Animal hybrid
class LivingThing:
    def breathe(self):
        print("Breathes air")

class Mammal(LivingThing):
    def feed_milk(self):
        print("Feeds milk to babies")

class Bird(LivingThing):
    def lay_eggs(self):
        print("Lays eggs")

class Bat(Mammal, Bird):
    def fly(self):
        print("Bat can fly")

bat = Bat()
bat.breathe()
bat.feed_milk()
bat.lay_eggs()
bat.fly()

# Example 3: Education hybrid
class Institution:
    def info(self):
        print("Institution: Ethiraj College")

class Course(Institution):
    def course_name(self):
        print("Course: B.Sc Computer Science")

class Sports(Institution):
    def sport(self):
        print("Sport: Cricket")

class Learner(Course, Sports):
    def details(self):
        print("Learner enrolled in course and sports")

l = Learner()
l.info()
l.course_name()
l.sport()
l.details()
