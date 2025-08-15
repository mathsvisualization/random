"""
==================================
Loops in Python
==================================

Loops are used to execute a block of code repeatedly
until a certain condition is met.
"""

# ==============================
# for loop with range()
# ==============================
for i in range(5):
    print("Iteration:", i)
# Output:
# Iteration: 0
# Iteration: 1
# Iteration: 2
# Iteration: 3
# Iteration: 4

# ==============================
# for loop over a list
# ==============================
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry

# ==============================
# while loop
# ==============================
count = 0
while count < 3:
    print("Count:", count)
    count += 1
# Output:
# Count: 0
# Count: 1
# Count: 2

# ==============================
# Loop control: break
# ==============================
for i in range(10):
    if i == 5:
        break
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4

# ==============================
# Loop control: continue
# ==============================
for i in range(5):
    if i == 2:
        continue
    print(i)
# Output:
# 0
# 1
# 3
# 4

# ==============================
# Loop control: pass
# ==============================
for i in range(3):
    pass  # placeholder for future code
# Output: (No output since pass does nothing)
