class Employee:
    def __init__(self, name, position):
        # Initialize attributes
        self.name = name
        self.position = position

    def get_details(self):
        """Display the employee's details."""
        print(f"Name: {self.name}, Position: {self.position}")


class Manager(Employee):
    def __init__(self, name, position, department):
        # Use super() to initialize inherited attributes
        super().__init__(name, position)
        self.department = department

    def get_details(self):
        """Display the manager's details, including department."""
        super().get_details()
        print(f"Department: {self.department}")


# Create instances and demonstrate
employee = Employee("John Doe", "Developer")
manager = Manager("Jane Smith", "Manager", "IT")

print("Employee Details:")
employee.get_details()

print("\nManager Details:")
manager.get_details()
