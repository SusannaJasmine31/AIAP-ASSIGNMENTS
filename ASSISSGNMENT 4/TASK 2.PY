def cm_to_inches(centimeters):
    """
    Convert centimeters to inches (1 inch = 2.54 cm).
    """
    if not isinstance(centimeters, (int, float)):
        raise TypeError("centimeters must be a number")
    if centimeters < 0:
        raise ValueError("centimeters cannot be negative")
    return centimeters / 2.54

if __name__ == "__main__":
    # Example: 10 cm -> 3.937"
    print(f'10 -> {cm_to_inches(10):.3f}"')