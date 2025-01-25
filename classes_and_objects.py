# Classes and Objects

# Define a base class 'Animal'
class Animal:
    def __init__(self, name, species):
        self.name = name  # Initialize the name attribute
        self.species = species  # Initialize the species attribute

    def speak(self):
        pass  # This method will be overridden in subclasses

    def info(self):
        return f"{self.name} is a {self.species}"  # Return basic information about the animal

# Define a subclass 'Dog' that inherits from 'Animal'
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")  # Call the constructor of the base class
        self.breed = breed  # Initialize the breed attribute

    def speak(self):
        return f"{self.name} says Woof!"  # Override the speak method

    def info(self):
        return f"{self.name} is a {self.breed} {self.species}"  # Return detailed information about the dog

# Define a subclass 'Cat' that inherits from 'Animal'
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Cat")  # Call the constructor of the base class
        self.color = color  # Initialize the color attribute

    def speak(self):
        return f"{self.name} says Meow!"  # Override the speak method

    def info(self):
        return f"{self.name} is a {self.color} {self.species}"  # Return detailed information about the cat

# Create instances of Dog and Cat
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Black")

# Call the speak and info methods on the instances
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!
print(dog.info())   # Output: Buddy is a Golden Retriever Dog
print(cat.info())   # Output: Whiskers is a Black Cat

# Creating more instances
dog2 = Dog("Max", "Bulldog")
cat2 = Cat("Luna", "White")

# Call the speak and info methods on the new instances
print(dog2.speak())  # Output: Max says Woof!
print(cat2.speak())  # Output: Luna says Meow!
print(dog2.info())   # Output: Max is a Bulldog Dog
print(cat2.info())   # Output: Luna is a White Cat

# Adding more methods to Animal class
class Animal:
    def __init__(self, name, species, age):
        self.name = name  # Initialize the name attribute
        self.species = species  # Initialize the species attribute
        self.age = age  # Initialize the age attribute

    def speak(self):
        pass  # This method will be overridden in subclasses

    def info(self):
        return f"{self.name} is a {self.species} and is {self.age} years old"  # Return detailed information about the animal

    def birthday(self):
        self.age += 1  # Increment the age attribute
        return f"Happy Birthday {self.name}! You are now {self.age} years old."  # Return a birthday message

# Create instances of Dog and Cat with age
dog3 = Dog("Charlie", "Beagle")
cat3 = Cat("Mittens", "Gray")

# Call the info and birthday methods on the instances
print(dog3.info())  # Output: Charlie is a Beagle Dog and is 0 years old
print(cat3.info())  # Output: Mittens is a Gray Cat and is 0 years old

print(dog3.birthday())  # Output: Happy Birthday Charlie! You are now 1 years old.
print(cat3.birthday())  # Output: Happy Birthday Mittens! You are now 1 years old.

# Adding more attributes and methods to Dog and Cat classes
class Dog(Animal):
    def __init__(self, name, breed, age, favorite_toy):
        super().__init__(name, "Dog", age)  # Call the constructor of the base class
        self.breed = breed  # Initialize the breed attribute
        self.favorite_toy = favorite_toy  # Initialize the favorite toy attribute

    def speak(self):
        return f"{self.name} says Woof!"  # Override the speak method

    def info(self):
        return f"{self.name} is a {self.breed} {self.species} and loves {self.favorite_toy}"  # Return detailed information about the dog

class Cat(Animal):
    def __init__(self, name, color, age, favorite_food):
        super().__init__(name, "Cat", age)  # Call the constructor of the base class
        self.color = color  # Initialize the color attribute
        self.favorite_food = favorite_food  # Initialize the favorite food attribute

    def speak(self):
        return f"{self.name} says Meow!"  # Override the speak method

    def info(self):
        return f"{self.name} is a {self.color} {self.species} and loves {self.favorite_food}"  # Return detailed information about the cat

# Create instances of Dog and Cat with additional attributes
dog4 = Dog("Rocky", "Poodle", 3, "Ball")
cat4 = Cat("Shadow", "Tabby", 2, "Fish")

# Call the info method on the instances
print(dog4.info())  # Output: Rocky is a Poodle Dog and loves Ball
print(cat4.info())  # Output: Shadow is a Tabby Cat and loves Fish
