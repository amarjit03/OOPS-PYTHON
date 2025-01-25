# Inheritance

# Define a base class 'Vehicle'
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand  # Initialize the brand attribute
        self.model = model  # Initialize the model attribute
        self.year = year  # Initialize the year attribute

    def get_info(self):
        return f"Vehicle: {self.brand} {self.model}, Year: {self.year}"  # Return vehicle information

# Define a subclass 'Car' that inherits from 'Vehicle'
class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)  # Call the constructor of the base class
        self.doors = doors  # Initialize the doors attribute

    def get_info(self):
        return f"Car: {self.brand} {self.model}, Year: {self.year}, Doors: {self.doors}"  # Override the get_info method

# Define a subclass 'Motorcycle' that inherits from 'Vehicle'
class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, type_motorcycle):
        super().__init__(brand, model, year)  # Call the constructor of the base class
        self.type_motorcycle = type_motorcycle  # Initialize the type of motorcycle attribute

    def get_info(self):
        return f"Motorcycle: {self.brand} {self.model}, Year: {self.year}, Type: {self.type_motorcycle}"  # Override the get_info method

# Create instances of Car and Motorcycle
car = Car("Toyota", "Corolla", 2020, 4)
motorcycle = Motorcycle("Harley-Davidson", "Street 750", 2019, "Cruiser")

# Call the get_info method on the instances
print(car.get_info())  # Output: Car: Toyota Corolla, Year: 2020, Doors: 4
print(motorcycle.get_info())  # Output: Motorcycle: Harley-Davidson Street 750, Year: 2019, Type: Cruiser

# Creating more instances
car2 = Car("Honda", "Civic", 2021, 4)
motorcycle2 = Motorcycle("Yamaha", "MT-07", 2020, "Sport")

# Call the get_info method on the new instances
print(car2.get_info())  # Output: Car: Honda Civic, Year: 2021, Doors: 4
print(motorcycle2.get_info())  # Output: Motorcycle: Yamaha MT-07, Year: 2020, Type: Sport

# Adding more methods to Vehicle class
class Vehicle:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand  # Initialize the brand attribute
        self.model = model  # Initialize the model attribute
        self.year = year  # Initialize the year attribute
        self.mileage = mileage  # Initialize the mileage attribute

    def get_info(self):
        return f"Vehicle: {self.brand} {self.model}, Year: {self.year}, Mileage: {self.mileage} miles"  # Return vehicle information

    def drive(self, miles):
        self.mileage += miles  # Increment the mileage attribute
        return f"{self.brand} {self.model} driven for {miles} miles. Total mileage: {self.mileage} miles"  # Return a drive message

# Create instances of Car and Motorcycle with mileage
car3 = Car("Ford", "Mustang", 2018, 2)
motorcycle3 = Motorcycle("Ducati", "Panigale V4", 2021, "Superbike")

# Call the get_info and drive methods on the instances
print(car3.get_info())  # Output: Car: Ford Mustang, Year: 2018, Mileage: 0 miles
print(motorcycle3.get_info())  # Output: Motorcycle: Ducati Panigale V4, Year: 2021, Mileage: 0 miles

print(car3.drive(150))  # Output: Ford Mustang driven for 150 miles. Total mileage: 150 miles
print(motorcycle3.drive(200))  # Output: Ducati Panigale V4 driven for 200 miles. Total mileage: 200 miles

# Adding more attributes and methods to Car and Motorcycle classes
class Car(Vehicle):
    def __init__(self, brand, model, year, mileage, fuel_type):
        super().__init__(brand, model, year, mileage)  # Call the constructor of the base class
        self.fuel_type = fuel_type  # Initialize the fuel type attribute

    def get_info(self):
        return f"Car: {self.brand} {self.model}, Year: {self.year}, Mileage: {self.mileage} miles, Fuel: {self.fuel_type}"  # Override the get_info method

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, mileage, engine_capacity):
        super().__init__(brand, model, year, mileage)  # Call the constructor of the base class
        self.engine_capacity = engine_capacity  # Initialize the engine capacity attribute

    def get_info(self):
        return f"Motorcycle: {self.brand} {self.model}, Year: {self.year}, Mileage: {self.mileage} miles, Engine: {self.engine_capacity}cc"  # Override the get_info method

# Create instances of Car and Motorcycle with additional attributes
car4 = Car("Chevrolet", "Camaro", 2019, 5000, "Gasoline")
motorcycle4 = Motorcycle("Kawasaki", "Ninja ZX-6R", 2020, 3000, 636)

# Call the get_info method on the instances
print(car4.get_info())  # Output: Car: Chevrolet Camaro, Year: 2019, Mileage: 5000 miles, Fuel: Gasoline
print(motorcycle4.get_info())  # Output: Motorcycle: Kawasaki Ninja ZX-6R, Year: 2020, Mileage: 3000 miles, Engine: 636cc
