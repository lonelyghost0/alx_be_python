import math

class Shape:
    """Base class representing a generic geometric shape."""
    def area(self):
        """Base method to be overridden by subclasses."""
        raise NotImplementedError("Subclasses must override the area() method.")


class Rectangle(Shape):
    """Rectangle shape subclass."""
    def __init__(self, length: float, width: float):
        """Initialize rectangle dimensions."""
        self.length = length
        self.width = width

    def area(self):
        """Return the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Circle shape subclass."""
    def __init__(self, radius: float):
        """Initialize circle radius."""
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * (self.radius ** 2)


# --- Polymorphism Demo ---
if __name__ == "__main__":
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        # Polymorphism in action: same method name behaves differently
        print(f"The area of the {shape.__class__.__name__} is {shape.area():.2f}")
