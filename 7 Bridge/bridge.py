# Bridge allows us to avoid exponential complexity growth
# Bridge separates interface from its implementation

# Example:
# circle & square implementation using vector & raster methods
from abc import ABC


class Renderer(ABC):
    def render_circle(self, radius):
        pass

    def render_square(self, side):
        pass


class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing a circle with radius {radius}')

    def render_square(self, side):
        print(f'Drawing a square with side {side}')


class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing pixels for a circle with radius {radius}')

    def render_square(self, side):
        print(f'Drawing pixels for a square with side {side}')


class Shape:
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self):
        pass

    def resize(self, factor):
        pass


class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor



class Square(Shape):
    def __init__(self, renderer, side):
        super().__init__(renderer)
        self.side = side

    def draw(self):
        self.renderer.render_square(self.side)

    def resize(self, factor):
        self.side *= factor


if __name__ == '__main__':
    raster = RasterRenderer()
    vector = VectorRenderer()
    circle = Circle(vector, 5)
    circle.draw()
    circle.resize(3)
    circle.draw()
    
    circle = Circle(raster, 4)
    circle.draw()
    circle.resize(2)
    circle.draw()

    sq = Square(raster, 5)
    sq.draw()
    sq.resize(4)
    sq.draw()
