def binary_search(array, target):
    """
    Perform Binary Search on a sorted list to find the index of the target element.

    Binary Search works on the principle of 'divide and conquer'.
    It repeatedly divides the search range in half until the target
    is found or the range becomes empty.

    Steps:
    1. Start with two pointers: low (start of list) and high (end of list).
    2. Find the middle index: mid = (low + high) // 2.
    3. Compare the middle element with the target:
       - If equal, return the index (mid).
       - If middle element is smaller than target, search the right half.
       - If middle element is greater than target, search the left half.
    4. Repeat until the target is found or low > high.
    5. If not found, return -1.

    Note:
        The input list MUST be sorted for Binary Search to work correctly.

    Args:
        array (list): Sorted list of elements to search.
        target (int/float/str): The value to find.

    Returns:
        int: Index of the target element if found, otherwise -1.

    Time Complexity:
        O(log n) - because the search range is halved after each step.

    Example:
        >>> binary_search([1, 3, 5, 7, 9], 7)
        3
    """
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


data = binary_search(sorted([1, 2, 4, 33, 22, 56, 32, 21, 6, 5, 3, 11]), 33)
print(data)
