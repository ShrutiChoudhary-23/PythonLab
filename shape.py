
from abc import ABC, abstractmethod
import math
# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def __str__(self):
        pass

# Vector class
class Vector(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overload + operator
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # Overload == operator
    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    # Overload < operator using vector magnitude
    def __lt__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.magnitude() < other.magnitude()

    # Calculate magnitude
    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def area(self):
        return 0

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Circle class
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    # Calculate area
    def area(self):
        return math.pi * self.radius ** 2

    # Overload + to add circle areas
    def __add__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented

        combined_area = self.area() + other.area()
        new_radius = math.sqrt(combined_area / math.pi)
        return Circle(new_radius)

    # Overload < to compare areas
    def __lt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.area() < other.area()

    # Overload == to compare radii
    def __eq__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius == other.radius

    def __str__(self):
        return f"Circle(radius={self.radius:.2f})"


# Main program
v1 = Vector(3, 4)
v2 = Vector(2, 1)

print("Vector 1:", v1)
print("Vector 2:", v2)
print("Vector Addition:", v1 + v2)
print("Are vectors equal?", v1 == v2)
print("Is Vector 2 smaller than Vector 1?", v2 < v1)
print("Magnitude of Vector 1:", v1.magnitude())

c1 = Circle(3)
c2 = Circle(4)

print("\nCircle 1:", c1)
print("Circle 2:", c2)
print("Area of Circle 1:", round(c1.area(), 2))
print("Area of Circle 2:", round(c2.area(), 2))
print("Combined Circle:", c1 + c2)
print("Is Circle 1 smaller than Circle 2?", c1 < c2)
print("Are circles equal?", c1 == c2)

