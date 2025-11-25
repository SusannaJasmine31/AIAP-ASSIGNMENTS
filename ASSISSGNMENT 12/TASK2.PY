def bubble_sort(lst):
    """
    Sort a list using the Bubble Sort algorithm.
    
    Args:
        lst: The list to sort
    
    Returns:
        The sorted list
    """
    n = len(lst)
    # Traverse through all list elements
    for i in range(n):
        # Last i elements are already in place
        swapped = False
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        # If no swapping occurred, list is already sorted
        if not swapped:
            break
    return lst


# Example usage and output verification
if __name__ == "__main__":
    # Test with unsorted list
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", numbers)
    
    # Create a copy to sort
    sorted_numbers = numbers.copy()
    bubble_sort(sorted_numbers)
    
    print("Sorted list:", sorted_numbers)
    
    # Verify the output is sorted
    is_sorted = all(sorted_numbers[i] <= sorted_numbers[i + 1] for i in range(len(sorted_numbers) - 1))
    print("Is sorted correctly?", is_sorted)
