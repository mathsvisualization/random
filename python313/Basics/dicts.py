"""
==================================
Dictionaries in Python
==================================
- Creation
- Access
- Methods
- dir() exploration
"""

d = {"name": "Alex", "age": 21}
print("Dict:", d)  # Dict: {'name': 'Alex', 'age': 21}

print("Access by key:", d["name"])  # Access by key: Alex
print("Get method:", d.get("age"))  # Get method: 21

d["age"] = 22
print("Update value:", d)  # Update value: {'name': 'Alex', 'age': 22}

d["city"] = "Delhi"
print("Add new:", d)  # Add new: {'name': 'Alex', 'age': 22, 'city': 'Delhi'}

print("Keys:", list(d.keys()))  # Keys: ['name', 'age', 'city']
print("Values:", list(d.values()))  # Values: ['Alex', 22, 'Delhi']
print("Items:", list(d.items()))  # Items: [('name', 'Alex'), ('age', 22), ('city', 'Delhi')]

d.pop("age")
print("After pop:", d)  # After pop: {'name': 'Alex', 'city': 'Delhi'}

print("Dict methods:", dir(d))
# Shortened output: ['clear', 'copy', 'fromkeys', ..., 'values']