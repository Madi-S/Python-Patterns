# LSP - Liskov Substitution Principle


class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    @property
    def area(self):
        return self._height * self._width

    def __str__(self):
        return f'Width: {self._width}, Height: {self._height}'

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


def use_it(rc):
    w = rc.width
    rc.height = 10
    expected_area = w * 10
    print(f'Expected area of {expected_area}, but got {rc.area}')


if __name__ == '__main__':
    rc = Rectangle(2, 3)
    use_it(rc)

    sq = Square(5)
    use_it(sq)

# The principle defines that objects of a superclass shall be replaceable with objects of its subclasses without breaking the application
# However, in our case classes Square and Rectangle are not replaceable, because the expected area of square differs from its actual one
# We change square's height, but with that we also change square's width, which breaks the program
# Hence, rectangle logic area calculation is not applicable for square area calculation logic
