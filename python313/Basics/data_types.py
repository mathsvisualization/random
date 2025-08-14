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