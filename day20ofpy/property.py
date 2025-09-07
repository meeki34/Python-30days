# property() = Decorator used to define a method as a property (it can be accessed like an attribute)
# Benefit: Add additional logic when reading, writing, or deleting attributes

# Gives you getter, setter and deleter functions for a data attribute
# property() = function that returns a property object

class Rectangle:
    def __init__(self, width, height):
        # These are the "protected" attributes, intended for internal use.
        self._width = width
        self._height = height

    # This is the "getter" method for the 'width' property.
    # It's called when you access `rectangle.width`.
    @property
    def width(self):
        print("-> Getting width")
        return self._width

    # This is the "setter" method for the 'width' property.
    # It's called when you assign a value, like `rectangle.width = 30`.
    @width.setter
    def width(self, value):
        print(f"-> Setting width to {value}")
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value

    # This is the "getter" for the 'height' property.
    @property
    def height(self):
        print("-> Getting height")
        return self._height

    # This is the "setter" for the 'height' property.
    @height.setter
    def height(self, value):
        print(f"-> Setting height to {value}")
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value

rectangle = Rectangle(10, 20)

# Now, we access the public properties (without the underscore).
# This automatically calls the "getter" methods defined with @property.
print(f"Initial width: {rectangle.width}")
print(f"Initial height: {rectangle.height}")

print("-" * 20)

# This calls the "setter" methods defined with @width.setter and @height.setter.
rectangle.width = 30
rectangle.height = 40

print(f"New width: {rectangle.width}")
print(f"New height: {rectangle.height}")