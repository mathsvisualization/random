"""
==================================
Strings in Python
==================================
- String creation
- Indexing & slicing
- String methods (commonly used)
- dir() to explore available methods
"""

# String creation
name = "John"
print("Name:", name)  # Name: John

# Indexing & slicing
print("First character:", name[0])  # First character: S
print("Last 3 characters:", name[-3:])  # Last 3 characters: vez
print("Reversed:", name[::-1])  # Reversed: zevahS

# dir() → shows all methods for strings
print("Available string methods:", dir(name))  
# Output (shortened): ['capitalize', 'casefold', 'center', ..., 'upper', 'zfill']

# Common methods
print("Uppercase:", name.upper())  # Uppercase: SHAVEZ
print("Lowercase:", name.lower())  # Lowercase: shavez
print("Title case:", name.title())  # Title case: Shavez
print("Starts with S:", name.startswith("S"))  # Starts with S: True
print("Ends with z:", name.endswith("z"))  # Ends with z: True
print("Count of 'a':", name.count("a"))  # Count of 'a': 1
print("Find 'vez':", name.find("vez"))  # Find 'vez': 3
print("Replace a -> @:", name.replace("a", "@"))  # Replace a -> @: Sh@vez
print("Split:", "hello world python".split())  # Split: ['hello', 'world', 'python']
print("Join:", "-".join(["2025", "08", "16"]))  # Join: 2025-08-16
print("Strip:", "   hi   ".strip())  # Strip: hi