from functools import reduce

s = [1, 2, 3, 4, 5, 6, 7]

# Lambda - a short, unnamed function
square = lambda x: x**2
print(square(5))

# Map - apply a function to every item
cubes = list(map(lambda a: a**3, s))
print(cubes)

# Filter - keep only items matching a condition
evens = list(filter(lambda a: a % 2 == 0, s))
print(evens)

# Reduce - combine all items into one value
total = reduce(lambda a, b: a + b, s)
print(total)
