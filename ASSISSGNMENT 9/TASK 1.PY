def calculate_even_odd_sums(numbers):
    """Calculate the sum of even and odd numbers in a list.

    This function takes a list of integers and computes the total sum of all
    even numbers and the total sum of all odd numbers separately.

    Args:
        numbers (list): A list of integers to process and calculate sums.

    Returns:
        tuple: A tuple of two integers (even_sum, odd_sum) where:
            - even_sum: Sum of all even numbers in the list
            - odd_sum: Sum of all odd numbers in the list

    Raises:
        TypeError: If the list contains non-numeric values.

    Examples:
        >>> calculate_even_odd_sums([1, 2, 3, 4, 5, 6])
        (12, 9)
        >>> calculate_even_odd_sums([10, 15, 20, 25])
        (30, 40)
        >>> calculate_even_odd_sums([])
        (0, 0)

    Note:
        - Works with positive and negative integers
        - Empty list returns (0, 0)
        - Zero is considered an even number
    """
    even_sum = sum(num for num in numbers if num % 2 == 0)
    odd_sum = sum(num for num in numbers if num % 2 != 0)
    return even_sum, odd_sum


# ============================================================================
# AI-GENERATED DOCSTRING (for comparison)
# ============================================================================
# def calculate_even_odd_sums(numbers):
#     """Compute sum of even and odd numbers from a given list.
#
#     Parameters:
#         numbers (List[int]): A list of integers to sum.
#
#     Returns:
#         Tuple[int, int]: A tuple containing the sum of even numbers and
#             the sum of odd numbers respectively.
#
#     Raises:
#         TypeError: If input contains non-integer values.
#
#     Examples:
#         >>> calculate_even_odd_sums([1, 2, 3, 4, 5, 6])
#         (12, 9)
#     """


# ============================================================================
# DOCSTRING COMPARISON
# ============================================================================
# MANUAL DOCSTRING:
# - Detailed description of function purpose
# - Uses "Args", "Returns", "Raises", "Examples", "Note" sections (Google Style)
# - More comprehensive with edge case documentation
# - Includes multiple examples
# - Explains what each return value represents
# - Mentions handling of zero and negative numbers
#
# AI-GENERATED DOCSTRING:
# - More concise and technical
# - Uses type hints in parameter/return descriptions (Tuple[int, int])
# - Cleaner, more minimal format
# - Includes basic documentation structure
# - Shorter examples section
# - Focuses on essential information only
#
# KEY DIFFERENCES:
# 1. Length: Manual is more detailed; AI is concise
# 2. Style: Manual follows Google Style strictly; AI is more flexible
# 3. Examples: Manual has 3 examples; AI has 1 example
# 4. Additional Notes: Manual includes edge cases; AI is straightforward
# 5. Readability: Manual is better for beginners; AI for experienced developers


# ============================================================================
# TEST CASES
# ============================================================================
if __name__ == "__main__":
    # Test case 1: Mixed even and odd numbers
    test1 = [1, 2, 3, 4, 5, 6]
    result1 = calculate_even_odd_sums(test1)
    print(f"Test 1: {test1}")
    print(f"Result: Even sum = {result1[0]}, Odd sum = {result1[1]}\n")

    # Test case 2: Only even numbers
    test2 = [10, 20, 30]
    result2 = calculate_even_odd_sums(test2)
    print(f"Test 2: {test2}")
    print(f"Result: Even sum = {result2[0]}, Odd sum = {result2[1]}\n")

    # Test case 3: Only odd numbers
    test3 = [1, 3, 5, 7]
    result3 = calculate_even_odd_sums(test3)
    print(f"Test 3: {test3}")
    print(f"Result: Even sum = {result3[0]}, Odd sum = {result3[1]}\n")

    # Test case 4: Empty list
    test4 = []
    result4 = calculate_even_odd_sums(test4)
    print(f"Test 4: {test4}")
    print(f"Result: Even sum = {result4[0]}, Odd sum = {result4[1]}\n")

    # Test case 5: Negative numbers
    test5 = [-4, -3, -2, -1, 2, 3]
    result5 = calculate_even_odd_sums(test5)
    print(f"Test 5: {test5}")
    print(f"Result: Even sum = {result5[0]}, Odd sum = {result5[1]}")