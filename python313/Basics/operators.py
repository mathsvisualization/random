"""
==================================
Python Operators
==================================

In Python, operators are special symbols that perform operations
on variables and values. Operators are categorized into different types
based on their functionality.
"""

# ==============================
# 1. Arithmetic Operators
# ==============================
a = 10
b = 3

# Example usage
print(a + b)   # Addition → 13
print(a - b)   # Subtraction → 7
print(a * b)   # Multiplication → 30
print(a / b)   # Division → 3.333...
print(a // b)  # Floor Division → 3
print(a % b)   # Modulus → 1
print(a ** b)  # Exponentiation → 1000

# ==============================
# 2. Comparison (Relational) Operators
# ==============================
print(a == b)   # Equal to → False
print(a != b)   # Not equal to → True
print(a > b)    # Greater than → True
print(a < b)    # Less than → False
print(a >= b)   # Greater than or equal to → True
print(a <= b)   # Less than or equal to → False

# ==============================
# 3. Logical Operators
# ==============================
x = True
y = False

print(x and y)  # Logical AND → False
print(x or y)   # Logical OR → True
print(not x)    # Logical NOT → False

# ==============================
# 4. Assignment Operators
# ==============================
num = 5
num += 3   # Same as: num = num + 3
print(num)  # 8

num -= 2
print(num)  # 6

num *= 4
print(num)  # 24

num //= 5
print(num)  # 4

num %= 3
print(num)  # 1

num **= 4
print(num)  # 1

# ==============================
# 5. Bitwise Operators
# ==============================
p = 5  # 101 (binary)
q = 3  # 011 (binary)

print(p & q)   # Bitwise AND → 1  (001)
print(p | q)   # Bitwise OR  → 7  (111)
print(p ^ q)   # Bitwise XOR → 6  (110)
print(~p)      # Bitwise NOT → -6
print(p << 2)  # Left shift  → 20 (10100)
print(p >> 1)  # Right shift → 2  (10)

# ==============================
# 6. Membership Operators
# ==============================
nums = [1, 2, 3, 4]
print(2 in nums)      # True
print(5 not in nums)  # True

# ==============================
# 7. Identity Operators
# ==============================
m = [1, 2, 3]
n = [1, 2, 3]
o = m

print(m is n)      # False (different objects, same value)
print(m is o)      # True  (same object in memory)
print(m is not n)  # True
