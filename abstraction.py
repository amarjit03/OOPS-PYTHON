# Abstraction

# Import the ABC and abstractmethod from the abc module
from abc import ABC, abstractmethod

# Define an abstract base class 'Shape'
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Abstract method that must be implemented by subclasses

    @abstractmethod
    def perimeter(self):
        pass  # Another abstract method for perimeter

# Define a subclass 'Rectangle' that inherits from 'Shape'
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width  # Initialize the width attribute
        self.height = height  # Initialize the height attribute

    def area(self):
        return self.width * self.height  # Implement the area method

    def perimeter(self):
        return 2 * (self.width + self.height)  # Implement the perimeter method

# Create an instance of Rectangle
rectangle = Rectangle(5, 10)

# Call the area and perimeter methods on the instance
print(rectangle.area())  # Output: 50
print(rectangle.perimeter())  # Output: 30

# Define another subclass 'Circle' that inherits from 'Shape'
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius  # Initialize the radius attribute

    def area(self):
        return 3.14 * self.radius * self.radius  # Implement the area method

    def perimeter(self):
        return 2 * 3.14 * self.radius  # Implement the perimeter method

# Create an instance of Circle
circle = Circle(7)

# Call the area and perimeter methods on the instance
print(circle.area())  # Output: 153.86
print(circle.perimeter())  # Output: 43.96

# Add a description method to the Shape class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def description(self):
        pass  # Abstract method for description

# Update the Rectangle class to include the description method
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def description(self):
        return f"Rectangle with width {self.width} and height {self.height}"

# Update the Circle class to include the description method
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def description(self):
        return f"Circle with radius {self.radius}"

# Create instances of the updated classes
rectangle2 = Rectangle(8, 12)
circle2 = Circle(10)

# Call the description, area, and perimeter methods on the instances
print(rectangle2.description())  # Output: Rectangle with width 8 and height 12
print(rectangle2.area())  # Output: 96
print(rectangle2.perimeter())  # Output: 40

print(circle2.description())  # Output: Circle with radius 10
print(circle2.area())  # Output: 314.0
print(circle2.perimeter())  # Output: 62.8
