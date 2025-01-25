# Polymorphism

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"

def animal_sound(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()
cow = Cow()

animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
animal_sound(cow)  # Output: Moo!

# Creating more instances
dog2 = Dog()
cat2 = Cat()
cow2 = Cow()

animal_sound(dog2)  # Output: Woof!
animal_sound(cat2)  # Output: Meow!
animal_sound(cow2)  # Output: Moo!

# Adding more methods to Animal class
class Animal:
    def speak(self):
        pass

    def move(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

    def move(self):
        return "Dog runs"

class Cat(Animal):
    def speak(self):
        return "Meow!"

    def move(self):
        return "Cat jumps"

class Cow(Animal):
    def speak(self):
        return "Moo!"

    def move(self):
        return "Cow walks"

def animal_action(animal):
    print(animal.speak())
    print(animal.move())

dog3 = Dog()
cat3 = Cat()
cow3 = Cow()

animal_action(dog3)  # Output: Woof! Dog runs
animal_action(cat3)  # Output: Meow! Cat jumps
animal_action(cow3)  # Output: Moo! Cow walks

# Adding more animals
class Bird(Animal):
    def speak(self):
        return "Chirp!"

    def move(self):
        return "Bird flies"

bird = Bird()
animal_action(bird)  # Output: Chirp! Bird flies

# Using polymorphism with a list of animals
animals = [Dog(), Cat(), Cow(), Bird()]

for animal in animals:
    animal_action(animal)
    # Output:
    # Woof! Dog runs
    # Meow! Cat jumps
    # Moo! Cow walks
    # Chirp! Bird flies

# Adding more attributes and methods to Animal class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

    def move(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

    def move(self):
        return f"{self.name} runs"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

    def move(self):
        return f"{self.name} jumps"

class Cow(Animal):
    def speak(self):
        return f"{self.name} says Moo!"

    def move(self):
        return f"{self.name} walks"

dog4 = Dog("Buddy")
cat4 = Cat("Whiskers")
cow4 = Cow("Bessie")

animal_action(dog4)  # Output: Buddy says Woof! Buddy runs
animal_action(cat4)  # Output: Whiskers says Meow! Whiskers jumps
animal_action(cow4)  # Output: Bessie says Moo! Bessie walks
