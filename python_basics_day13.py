# Day 13 - Duck Typing (3 examples)

# Example 1: Two unrelated classes with the same method name
class Duck:
    def sound(self):
        print("Duck says Quack")

class Human:
    def sound(self):
        print("Human says Hello")

def make_it_talk(thing):
    thing.sound()   # Python doesn't care what type 'thing' is, only that it has sound()

make_it_talk(Duck())
make_it_talk(Human())

# Example 2: Different objects behaving the same way in a loop
class Car:
    def move(self):
        print("Car drives on the road")

class Boat:
    def move(self):
        print("Boat sails on water")

class Plane:
    def move(self):
        print("Plane flies in the sky")

for vehicle in [Car(), Boat(), Plane()]:
    vehicle.move()

# Example 3: Duck typing with built-in functions (works on anything with len())
class Basket:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

b = Basket(["apple", "banana", "mango"])
print(len(b))        # works because Basket defines __len__
print(len("Monisha"))   # works on string
print(len([1, 2, 3]))   # works on list
