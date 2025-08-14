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