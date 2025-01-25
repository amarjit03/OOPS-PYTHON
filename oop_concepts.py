# 1. Classes and Objects

# Define a base class 'Animal'
class Animal:
    def __init__(self, name):
        self.name = name  # Initialize the name attribute

    def speak(self):
        pass  # This method will be overridden in subclasses

# Define a subclass 'Dog' that inherits from 'Animal'
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"  # Override the speak method

# Define a subclass 'Cat' that inherits from 'Animal'
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"  # Override the speak method

# Create instances of Dog and Cat
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Call the speak method on the instances
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!

# 2. Inheritance

# Define a base class 'Vehicle'
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand  # Initialize the brand attribute
        self.model = model  # Initialize the model attribute

    def get_info(self):
        return f"Vehicle: {self.brand} {self.model}"  # Return vehicle information

# Define a subclass 'Car' that inherits from 'Vehicle'
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)  # Call the constructor of the base class
        self.doors = doors  # Initialize the doors attribute

    def get_info(self):
        return f"Car: {self.brand} {self.model}, Doors: {self.doors}"  # Override the get_info method

# Create an instance of Car
car = Car("Toyota", "Corolla", 4)

# Call the get_info method on the instance
print(car.get_info())  # Output: Car: Toyota Corolla, Doors: 4

# 3. Polymorphism

# Define a function that takes an animal and calls its speak method
def animal_sound(animal):
    print(animal.speak())

# Call the animal_sound function with different types of animals
animal_sound(dog)  # Output: Buddy says Woof!
animal_sound(cat)  # Output: Whiskers says Meow!

# 4. Encapsulation

# Define a class 'Person' with private attributes
class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    def get_name(self):
        return self.__name  # Getter method for name

    def get_age(self):
        return self.__age  # Getter method for age

# Create an instance of Person
person = Person("Alice", 30)

# Call the getter methods on the instance
print(person.get_name())  # Output: Alice
print(person.get_age())   # Output: 30

# 5. Abstraction

# Import the ABC and abstractmethod from the abc module
from abc import ABC, abstractmethod

# Define an abstract base class 'Shape'
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Abstract method that must be implemented by subclasses

# Define a subclass 'Rectangle' that inherits from 'Shape'
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width  # Initialize the width attribute
        self.height = height  # Initialize the height attribute

    def area(self):
        return self.width * self.height  # Implement the area method

# Create an instance of Rectangle
rectangle = Rectangle(5, 10)

# Call the area method on the instance
print(rectangle.area())  # Output: 50
