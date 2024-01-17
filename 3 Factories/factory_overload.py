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
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'(x: {self.x}, y: {self.y})'

    class PointFactory:
        def new_cartesian_point(self, x, y):
            p = Point()
            p.x = x
            p.y = y
            return p

        def new_polar_point(self, rho, theta):
            p = Point()
            p.x = rho * cos(theta)
            p.y = rho * sin(theta)
            return p

    factory = PointFactory()


if __name__ == '__main__':
    p = Point(2, 3)
    p2 = Point.factory.new_polar_point(4, 5)
    print(p, p2)
