"""
==================================
Lists in Python
==================================
- Creation
- Indexing & slicing
- Methods
- dir() exploration
"""

nums = [1, 2, 3, 4]
print("List:", nums)  # List: [1, 2, 3, 4]

# Indexing & slicing
print("First:", nums[0])  # First: 1
print("Last two:", nums[-2:])  # Last two: [3, 4]

# dir()
print("Available methods:", dir(nums))
# Shortened output: ['append', 'clear', 'copy', ..., 'sort']

# Methods
nums.append(5)
print("Append:", nums)  # Append: [1, 2, 3, 4, 5]

nums.insert(1, 10)
print("Insert:", nums)  # Insert: [1, 10, 2, 3, 4, 5]

nums.remove(3)
print("Remove:", nums)  # Remove: [1, 10, 2, 4, 5]

popped = nums.pop()
print("Pop:", nums, "| Popped:", popped)  
# Pop: [1, 10, 2, 4] | Popped: 5

nums.sort()
print("Sorted:", nums)  # Sorted: [1, 2, 4, 10]

nums.reverse()
print("Reversed:", nums)  # Reversed: [10, 4, 2, 1]

copy_list = nums.copy()
print("Copy:", copy_list)  # Copy: [10, 4, 2, 1]

nums.clear()
print("Cleared:", nums)  # Cleared: []