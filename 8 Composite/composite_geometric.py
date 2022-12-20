# Composite pattern is used for using the same interface through inheritance
# It also allows us to deal with various data types in the same way
# Like implementing magic methods, such as, __iter__ or Iterable


class GraphicalObject:
    def __init__(self, color=None):
        self.color = color
        self.children = []
        self._name = 'Group'

    @property
    def name(self):
        return self._name

    def _print(self, items, depth):
        items.append('*' * depth)
        if self.color:
            items.append(self.color + ' ')
        items.append(self.name + '\n')
        for child in self.children:
            child._print(items, depth + 1)

    def __str__(self):
        items = []
        self._print(items, 0)
        return ''.join(items)


class Circle(GraphicalObject):
    @property
    def name(self):
        return 'Circle'


class Square(GraphicalObject):
    @property
    def name(self):
        return 'Square'


if __name__ == '__main__':
    drawing = GraphicalObject()
    drawing._name = 'My Drawing'
    drawing.children.append(Circle('Red'))
    drawing.children.append(Square('Green'))

    group = GraphicalObject()
    group.children.append(Circle('Blue'))
    group.children.append(Square('Blue'))

    drawing.children.append(group)
    print(drawing)
