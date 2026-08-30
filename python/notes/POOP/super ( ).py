# super() = Function used in a chiled class to call methods/attributes from a parent class (superclass).
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

    def describe(self):                                                             # if a method of same name exists in both children calss and parent class, then children
        print(f"This is a circle with area {3.14 * pow(self.radius, 2)}")           # class will have more priority
        super().describe()

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
circle = Circle("red", False, 2)
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


