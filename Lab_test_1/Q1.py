def factorial(n):
    """
    Calculate the factorial of a number.
    
    The factorial of n (denoted as n!) is the product of all positive integers
    less than or equal to n. By definition, 0! = 1.
    
    Args:
        n (int): A non-negative integer
        
    Returns:
        int: The factorial of n
        
    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer
        
    Examples:
        >>> factorial(0)
        1
        >>> factorial(5)
        120
        >>> factorial(-1)
        Traceback (most recent call last):
        ...
        ValueError: Factorial is not defined for negative numbers
    """
    # Type checking
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, got {type(n).__name__}")
    
    # Handle negative input
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    # Handle zero case (0! = 1 by definition)
    if n == 0:
        return 1
    
    # Calculate factorial for positive integers
    result = 1
    for i in range(1, n + 1):
        result *= i
    
    return result


def main():
    """Demonstrate the factorial function with various test cases."""
    
    print("=" * 50)
    print("Factorial Function - Test Cases")
    print("=" * 50)
    
    # Test cases covering different scenarios
    test_cases = [
        (0, "Zero case (0! = 1)"),
        (1, "Base case (1! = 1)"),
        (5, "Small positive number"),
        (10, "Larger positive number"),
        (-5, "Negative number (should raise error)"),
        (3.5, "Non-integer (should raise error)")
    ]
    
    for value, description in test_cases:
        print(f"\nTest: {description}")
        print(f"Input: {value}")
        try:
            result = factorial(value)
            print(f"Result: {result}")
        except (ValueError, TypeError) as e:
            print(f"Error: {e}")
    
    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
