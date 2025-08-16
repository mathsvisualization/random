"""
==================================
Tuples & Sets in Python
==================================
- Tuples
- Sets
- dir() exploration
"""

# Tuple
t = (1, 2, 3, 2)
print("Tuple:", t)  # Tuple: (1, 2, 3, 2)

print("First elem:", t[0])  # First elem: 1
print("Count of 2:", t.count(2))  # Count of 2: 2
print("Index of 3:", t.index(3))  # Index of 3: 2
print("Tuple methods:", dir(t))  
# ['count', 'index', ...]

# Set
s = {1, 2, 3, 4}
print("Set:", s)  # Set: {1, 2, 3, 4}

s.add(5)
print("Add:", s)  # Add: {1, 2, 3, 4, 5}

s.remove(2)
print("Remove:", s)  # Remove: {1, 3, 4, 5}

s.update([6, 7])
print("Update:", s)  # Update: {1, 3, 4, 5, 6, 7}

print("Union:", s.union({10, 11}))  # Union: {1, 3, 4, 5, 6, 7, 10, 11}
print("Intersection:", s.intersection({5, 6}))  # Intersection: {5, 6}

print("Set methods:", dir(s))
# Shortened output: ['add', 'clear', 'copy', ..., 'union', 'update']
