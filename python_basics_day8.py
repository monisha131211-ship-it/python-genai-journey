# Day 8 - File Handling, Abstraction, Class (3 examples each)

# ================= FILE HANDLING (3 examples) =================

# Example 1: Writing to a file
with open("notes.txt", "w") as f:
    f.write("Day 8 of my Python + Generative AI journey\n")
    f.write("Learning file handling today")

# Example 2: Reading a file
with open("notes.txt", "r") as f:
    content = f.read()
    print(content)

# Example 3: Appending to a file
with open("notes.txt", "a") as f:
    f.write("\nAppended a new line successfully")

with open("notes.txt", "r") as f:
    print(f.read())



