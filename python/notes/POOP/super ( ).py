# super() = Function used in a chiled class to call methods from a parent class (superclass).
#             Allows you to extend the dunctionality of the inherited methods.

class Shapes:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")


class Circle(Shapes):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

class Square(Shapes):
    def __init__(self, color, is_filled, side):
        super().__init__(color, is_filled)
        self.side = side

class Rectangle(Shapes):
    def __init__(self, color, is_filled, length, breadth):
        super().__init__(color, is_filled)
        self.length = length
        self.breadth = breadth


rectangle = Rectangle("green", True, 5, 4)
circle = Circle("red", False, 1)
square = Square("blue", True, 10)

print(circle.color)
print(circle.is_filled)
print(circle.radius)
circle.describe()

print("---------------------------------------")

print(rectangle.color)
print(rectangle.is_filled)
print(rectangle.length)
print(rectangle.breadth)
rectangle.describe()

print("---------------------------------------")

print(square.color)
print(square.is_filled)
print(square.side)
square.describe()