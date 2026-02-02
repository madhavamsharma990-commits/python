import math

class Circle:
    """
    Represents a circle with methods to compute its area and perimeter.
    """
    def __init__(self, radius):
        """
        Initializes the Circle object with a given radius.

        Args:
            radius (float or int): The radius of the circle.
        """
        if not isinstance(radius, (int, float)) or radius <= 0:
            raise ValueError("Radius must be a positive number")
        self.radius = radius

    def area(self):
        """
        Computes the area of the circle using the formula A = π * r^2.

        Returns:
            float: The area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Computes the perimeter (circumference) of the circle using the formula C = 2 * π * r.

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * math.pi * self.radius

# --- Example Usage ---
if __name__ == "__main__":
    # Create a Circle object with a radius of 5
    my_circle = Circle(5)

    # Compute and print the area
    circle_area = my_circle.area()
    print(f"The area of the circle is: {circle_area:.2f}")

    # Compute and print the perimeter
    circle_perimeter = my_circle.perimeter()
    print(f"The perimeter of the circle is: {circle_perimeter:.2f}")

    # Example with a different radius
    another_circle = Circle(12.5)
    print(f"\nFor a circle with radius 12.5:")
    print(f"Area: {another_circle.area():.2f}")
    print(f"Perimeter: {another_circle.perimeter():.2f}")
