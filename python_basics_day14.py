# Day 14 - Pattern Programs in Python (10 patterns)

n = int(input("Enter the value: "))

print("\nPattern 1: Solid square of stars")
for i in range(n):
    for j in range(n):
        print("* ", end="")
    print()

print("\nPattern 2: Right triangle (increasing)")
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

print("\nPattern 3: Inverted right triangle (decreasing)")
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

print("\nPattern 4: Decreasing number triangle")
for i in range(n):
    for j in range(1, n - i):
        print(j, end="")
    print()

print("\nPattern 5: Increasing number triangle (0-indexed)")
for i in range(n):
    for j in range(i):
        print(j, end="")
    print()

print("\nPattern 6: Rows of repeated numbers")
for i in range(1, n + 1):
    for j in range(n):
        print(i, end="")
    print()

print("\nPattern 7: Pyramid of stars (centered)")
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

print("\nPattern 8: Floyd's triangle (continuous numbers)")
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

print("\nPattern 9: Number pyramid (centered)")
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\nPattern 10: Diamond of stars")
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

print("\nPattern 11: Heart")
for row in range(6):
    for col in range(7):
        if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0) or (row - col == 2) or (row + col == 8):
            print("*", end="")
        else:
            print(" ", end="")
    print()    
