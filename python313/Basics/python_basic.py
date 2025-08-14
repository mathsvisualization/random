"""
Python Basics Module

This module covers fundamental Python concepts, focusing
on basic data types, variables, and simple operations.

Author: Shavez
Date: 13/08/2025
"""

"""
==================================
Built-in Data Types in Python
==================================

In Python, every value has a type, which can be checked using the built-in `type()` function.
Below are the main built-in data types with examples.
"""

# 1️⃣ Numeric Types
my_int = 4                     # Integer
my_float = 4.8                 # Floating point
my_complex = 1 + 2j            # Complex number

# Example usage
print(type(my_int))      # Output: <class 'int'>
print(type(my_float))    # Output: <class 'float'>
print(type(my_complex))  # Output: <class 'complex'>


# 2️⃣ Sequence Types
my_str = "John"                                # String (immutable)
my_list = [1, 2, 3.4, "multiple objects"]     # List (mutable)
my_tuple = (3 + 4j, "ordered", 1.0)          # Tuple (immutable, ordered)

# Example usage
print(type(my_str))   # Output: <class 'str'>
print(type(my_list))  # Output: <class 'list'>
print(type(my_tuple)) # Output: <class 'tuple'>


# 3️⃣ Set Types
my_set = {1, 2, 3, "unordered", "unique"}               # Set (mutable, unordered, unique elements)
my_frozenset = frozenset({"immutable", "set", 1.0})    # Frozenset (immutable set)

# Example usage
print(type(my_set))       # Output: <class 'set'>
print(type(my_frozenset)) # Output: <class 'frozenset'>


# 4️⃣ Mapping Type
my_dict = {"key": "value", "mutable": 1.0}  # Dictionary (key-value mapping)

# Example usage
print(type(my_dict))  # Output: <class 'dict'>


# 5️⃣ Boolean Type
my_bool_true = True
my_bool_false = False

# Example usage
print(type(my_bool_true))   # Output: <class 'bool'>
print(type(my_bool_false))  # Output: <class 'bool'>


# 6️⃣ None Type
my_none = None

# Example usage
print(type(my_none))  # Output: <class 'NoneType'>


"""
===========================
Variables in Python
===========================

In Python, a variable is like a container that stores data or a value. 
You can use this value anytime by referring to the variable name.

Variables can be categorized mainly into two types:
1. Global Variables
2. Local Variables

---------------------------------
1. Global Variables
---------------------------------
- Defined outside all functions.
- Accessible anywhere in the code, inside or outside functions.

Example:
"""
x = 10  # Global variable

def print_global():
    """Accessing global variable inside function"""
    print("Global x:", x)

print_global()             # Output: Global x: 10
print("Outside function x:", x)  # Output: Outside function x: 10

"""
---------------------------------
2. Local Variables
---------------------------------
- Defined inside a function.
- Accessible only within that function.

Example:
"""
def my_function():
    y = 5  # Local variable
    print("Local y:", y)

my_function()  # Output: Local y: 5
# print(y)  # This would give an error because y is local to my_function

"""
---------------------------------
3. Rules for Naming Variables
---------------------------------
1. Variable names can contain letters, numbers, and underscores (_), but **cannot start with a number**.
   Examples:
       name = "Shavez"   # Valid
       _score = 100      # Valid
       age1 = 18         # Valid
       1age = 18         # Invalid

2. No spaces allowed in variable names. Use underscore for multiple words.
   Examples:
       first_name = "Shavez"  # Valid
       first name = "Shavez"  # Invalid

3. Special characters are not allowed (like @, $, %, -).
   Example:
       price$ = 100  # Invalid

4. Variable names are **case sensitive**.
   Examples:
       Age = 18
       age = 19
       print(Age, age)  # Output: 18 19

5. Reserved keywords cannot be used as variable names.
   Examples of keywords: for, if, while, def, return, class, etc.

---------------------------------
4. Summary
---------------------------------
- In Python, **declaring a variable = assigning it a value**.
- Global variables can be accessed anywhere.
- Local variables are accessible only within the function they are defined.
- Follow naming rules to avoid syntax errors.
"""