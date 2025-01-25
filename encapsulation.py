# Encapsulation

# Define a class 'Person' with private attributes
class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    def get_name(self):
        return self.__name  # Getter method for name

    def get_age(self):
        return self.__age  # Getter method for age

    def set_name(self, name):
        self.__name = name  # Setter method for name

    def set_age(self, age):
        if age > 0:
            self.__age = age  # Setter method for age with validation
        else:
            print("Age must be positive")  # Print an error message if age is not positive

# Create an instance of Person
person = Person("Alice", 30)

# Call the getter methods on the instance
print(person.get_name())  # Output: Alice
print(person.get_age())   # Output: 30

# Call the setter methods on the instance
person.set_name("Bob")
person.set_age(35)
print(person.get_name())  # Output: Bob
print(person.get_age())   # Output: 35

# Trying to set a negative age
person.set_age(-5)  # Output: Age must be positive

# Adding more methods to Person class
class Person:
    def __init__(self, name, age, address):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute
        self.__address = address  # Private attribute

    def get_name(self):
        return self.__name  # Getter method for name

    def get_age(self):
        return self.__age  # Getter method for age

    def get_address(self):
        return self.__address  # Getter method for address

    def set_name(self, name):
        self.__name = name  # Setter method for name

    def set_age(self, age):
        if age > 0:
            self.__age = age  # Setter method for age with validation
        else:
            print("Age must be positive")  # Print an error message if age is not positive

    def set_address(self, address):
        self.__address = address  # Setter method for address

# Create an instance of Person with address
person2 = Person("Charlie", 25, "123 Main St")

# Call the getter methods on the instance
print(person2.get_name())  # Output: Charlie
print(person2.get_age())   # Output: 25
print(person2.get_address())  # Output: 123 Main St

# Call the setter method for address on the instance
person2.set_address("456 Elm St")
print(person2.get_address())  # Output: 456 Elm St

# Adding more attributes and methods to Person class
class Person:
    def __init__(self, name, age, address, phone_number):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute
        self.__address = address  # Private attribute
        self.__phone_number = phone_number  # Private attribute

    def get_name(self):
        return self.__name  # Getter method for name

    def get_age(self):
        return self.__age  # Getter method for age

    def get_address(self):
        return self.__address  # Getter method for address

    def get_phone_number(self):
        return self.__phone_number  # Getter method for phone number

    def set_name(self, name):
        self.__name = name  # Setter method for name

    def set_age(self, age):
        if age > 0:
            self.__age = age  # Setter method for age with validation
        else:
            print("Age must be positive")  # Print an error message if age is not positive

    def set_address(self, address):
        self.__address = address  # Setter method for address

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number  # Setter method for phone number

# Create an instance of Person with phone number
person3 = Person("David", 40, "789 Oak St", "555-1234")

# Call the getter methods on the instance
print(person3.get_name())  # Output: David
print(person3.get_age())   # Output: 40
print(person3.get_address())  # Output: 789 Oak St
print(person3.get_phone_number())  # Output: 555-1234

# Call the setter method for phone number on the instance
person3.set_phone_number("555-5678")
print(person3.get_phone_number())  # Output: 555-5678
