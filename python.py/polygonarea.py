# Class for Triangle
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# Class for Rectangle
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


# Class for Square
class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


# Creating objects
triangle = Triangle(10, 5)
rectangle = Rectangle(8, 4)
square = Square(6)

# Printing areas
print("Area of Triangle:", triangle.area())
print("Area of Rectangle:", rectangle.area())
print("Area of Square:", square.area())
