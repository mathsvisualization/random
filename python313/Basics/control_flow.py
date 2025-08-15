"""
==================================
Control Flow Statements in Python
==================================

Control flow statements allow you to control the execution
path of your program based on conditions.
"""

# ==============================
# if statement
# ==============================
x = 10
if x > 5:
    print("x is greater than 5")

# ==============================
# if-else statement
# ==============================
y = 3
if y % 2 == 0:
    print("y is even")
else:
    print("y is odd")

# ==============================
# if-elif-else statement
# ==============================
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
else:
    print("Grade: C")

# ==============================
# Nested if
# ==============================
age = 20
if age >= 18:
    if age <= 25:
        print("You are a young adult")

# ==============================
# Short-hand if (ternary operator style)
# ==============================
num = 7
result = "Even" if num % 2 == 0 else "Odd"
print(result)
