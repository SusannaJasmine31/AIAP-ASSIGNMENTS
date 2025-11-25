import math

def calculate_area(shape, x, y=0):
    """
    Calculate the area of different shapes.
    
    Args:
        shape (str): The type of shape ('rectangle', 'square', 'circle')
        x (float): Width for rectangle, side for square, radius for circle
        y (float): Height for rectangle (optional, default=0)
    
    Returns:
        float: The calculated area
    
    Raises:
        ValueError: If shape is not recognized
    """
    shape = shape.lower()
    
    shapes = {
        "rectangle": lambda: x * y,
        "square": lambda: x ** 2,
        "circle": lambda: math.pi * x ** 2
    }
    
    if shape not in shapes:
        raise ValueError(f"Unknown shape: {shape}. Supported shapes: {', '.join(shapes.keys())}")
    
    return shapes[shape]()


# Example usage
if __name__ == "__main__":
    print(f"Rectangle (5x3): {calculate_area('rectangle', 5, 3)}")
    print(f"Square (4x4): {calculate_area('square', 4)}")
    print(f"Circle (r=3): {calculate_area('circle', 3)}")
