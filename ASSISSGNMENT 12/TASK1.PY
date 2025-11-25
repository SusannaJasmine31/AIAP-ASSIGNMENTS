def linear_search(lst, target):
    """
    Search for a value in a list and return its index.
    
    Args:
        lst: The list to search in
        target: The value to search for
    
    Returns:
        The index of the target value if found, -1 otherwise
    """
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1


# Example usage
if __name__ == "__main__":
    numbers = [10, 23, 45, 70, 11, 15]
    
    # Search for existing value
    result = linear_search(numbers, 70)
    if result != -1:
        print(f"Value found at index: {result}")
    else:
        print("Value not found")
    
    # Search for non-existing value
    result = linear_search(numbers, 99)
    if result != -1:
        print(f"Value found at index: {result}")
    else:
        print("Value not found")
