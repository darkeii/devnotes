# property = Decorator used to define a method as a property (it can be accessed like an attribute)
#           Benefit: Add additional logic when read, write or delete attributes
#                     Gives you getter , setter , and deleter method

class Rectangle:
    def __init__(self, width, height):
        self._width = width                     # using "_" like this ... makes the attribute private...
        self._height = height                   # which means the developer doesnt want the user to directly be able to access
                                                # the value of attribute by simple instance call methods.
    @property                                   # to access these we can use @property decorator... which will assign a logic to that output when the attribute is called.
    def width(self):
        return f"{self._width:.1f}cm"                       # getter methods

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    @width.setter                                           # setter methods
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than 0")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
           self._height = new_height
        else:
            print("Height must be greater than 0")

    @width.deleter                                      # deleter methods
    def width(self):
        del self._width
        print("Width has been cleared")

    @height.deleter
    def height(self):
        del self._height
        print("height has been cleared")


rectangle = Rectangle(3, 4)

rectangle.width = 5
rectangle.height = 10

print(rectangle.width)
print(rectangle.height)


del rectangle.width
del rectangle.height


