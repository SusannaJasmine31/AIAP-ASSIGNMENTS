class Car:
    """A class to represent a car."""
    
    def __init__(self, brand, model, year):
        """Initialize car attributes."""
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_details(self):
        """Display car details."""
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

# Create an object and call the method
car1 = Car("Toyota", "Camry", 2022)
car1.display_details()

# Create another object
car2 = Car("Honda", "Civic", 2023)
car2.display_details()