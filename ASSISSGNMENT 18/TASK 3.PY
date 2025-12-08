def factorial(n):
    """Calculate the factorial of a number using recursion."""
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Test cases
print(f"Factorial of 5: {factorial(5)}")  # Output: 120
print(f"Factorial of 0: {factorial(0)}")  # Output: 1