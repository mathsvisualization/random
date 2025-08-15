"""
==================================
Functions in Python
==================================

Functions are reusable blocks of code that perform a specific task.
They help in organizing code and avoiding repetition.
"""

# ==============================
# Basic function
# ==============================
def greet():
    print("Hello, world!")

greet()
# Output:
# Hello, world!

# ==============================
# Function with parameters
# ==============================
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Shavez")
# Output:
# Hello, Shavez!

# ==============================
# Function with default parameter
# ==============================
def greet_with_default(name="Guest"):
    print(f"Welcome, {name}!")

greet_with_default()
greet_with_default("Shavez")
# Output:
# Welcome, Guest!
# Welcome, Shavez!

# ==============================
# Function with return value
# ==============================
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)
# Output:
# Sum: 8

# ==============================
# Function with variable-length arguments
# ==============================
def sum_all(*numbers):
    return sum(numbers)

print("Total:", sum_all(1, 2, 3, 4))
# Output:
# Total: 10

# ==============================
# Function with keyword arguments
# ==============================
def introduce(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

introduce(name="Shavez", age=17, city="Delhi")
# Output:
# name: Shavez
# age: 17
# city: Delhi
