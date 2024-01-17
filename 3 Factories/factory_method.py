# Factory method solves optional parameters issue of objects initialization
# It allows us to initialize object in different ways as we wish
# This example demonstrates initialization of Point objects using (x, y) or (rho, theta) parameters
# Overall, factory methods just create new instances of the same class but with different parameters, etc
from enum import Enum
from math import sin, cos


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Bad approach, because it is open for modification
    # def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
        # if system == CoordinateSystem.CARTESIAN:
        #     self.x = a
        #     self.y = b
        # elif system == CoordinateSystem.POLAR:
        #     self.x = a * cos(b)
        #     self.y = a * sin(b)

    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))

    def __str__(self):
        return f'(x: {self.x}, y: {self.y})'


if __name__ == '__main__':
    p = Point(2, 3)
    p2 = Point.new_polar_point(4, 5)
    print(p, p2)
