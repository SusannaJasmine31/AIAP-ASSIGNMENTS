def check_number(num):
    """Check if a number is positive, negative, or zero."""
    if num < 0:
        return "The number is negative"
    elif num == 0:
        return "The number is zero"
    else:
        return "The number is positive"

# Test cases
print(check_number(-5))  # Output: The number is negative
print(check_number(0))   # Output: The number is zero
print(check_number(7))   # Output: The number is positive