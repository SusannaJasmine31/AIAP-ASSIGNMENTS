def fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number using recursion."""
    # Input validation
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be non-negative")
    
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    try:
        # Get input from user
        n = int(input("Enter a number to find its Fibonacci value: "))
        # Calculate and display result
        result = fibonacci(n)
        print(f"F({n}) = {result}")
        
    except ValueError as e:
        print("Please enter a valid non-negative integer")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()