class Rectangle:
    def __init__(self, length, width):
        """
        Initialize the Rectangle with length and width.
        """
        self.length = length
        self.width = width

    @property
    def area(self):
        """
        Calculate and return the area of the rectangle.
        """
        return self.length * self.width

    @property
    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.
        """
        return 2 * (self.length + self.width)

    def __str__(self):
        """
        String representation of the Rectangle instance.
        """
        return f"Rectangle(Length: {self.length}, Width: {self.width})"

    def __eq__(self, other):
        """
        Compare two Rectangle objects to check if their areas are equal.
        """
        if isinstance(other, Rectangle):
            return self.area == other.area
        return False


# Create two rectangle instances
rect1 = Rectangle(5, 3)
rect2 = Rectangle(4, 4)

# Demonstrate all methods
print("Rectangle 1:", rect1)  # Uses __str__()
print("Area of Rectangle 1:", rect1.area)  # Uses the area property
print("Perimeter of Rectangle 1:", rect1.perimeter)  # Uses the perimeter property

print("\nRectangle 2:", rect2)  # Uses __str__()
print("Area of Rectangle 2:", rect2.area)  # Uses the area property
print("Perimeter of Rectangle 2:", rect2.perimeter)  # Uses the perimeter property

# Compare the two rectangles using __eq__()
if rect1 == rect2:
    print("\nThe two rectangles have the same area.")
else:
    print("\nThe two rectangles do not have the same area.")
