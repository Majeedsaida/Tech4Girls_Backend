class Car:
    def __init__(self, make, model, year):
        # Instance variables
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        """Prints the car's details."""
        print(f"Car Make: {self.make}, Model: {self.model}, Year: {self.year}")


# Create an instance of the Car class
my_car = Car("Toyota", "Camry", 2020)

# Call the display_info method
my_car.display_info()
