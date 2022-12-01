# OCP - Open Closed Principle
# Classes should be open for extension (adding some new methods), but closed for modification (changing existing methods)


from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product():
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:
    def filter_by_color(self, products, color):
        for product in products:
            if product.color == color:
                yield product

    def filter_by_size(self, products, size):
        for product in products:
            if product.size == size:
                yield product

    def filter_by_size_and_color(self, products, size, color):
        for product in products:
            if product.size == size and product.color == color:
                yield product


# The abeve method is not scalable, too much methods to add for various filters (imagine or, and for different attributes)
# OCP = open for extension, but closed for modification
# Lets modify it with OCP


# Base classes (interfacec)
class Specification:
    def is_satisfied(self, item):
        pass

    # Binary and operator &
    def __and__(self, other):
        return AndSpecification(self, other)

    def __or__(self, other):
        return OrSpecification(self, other)


class Filter:
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        # Args are specifications, hence, we can write `spec.is_satisfied(item)`
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))


class OrSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        # Args are specifications, hence, we can write `spec.is_satisfied(item)`
        return any(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == '__main__':
    chair = Product('Chair', Color.RED, Size.MEDIUM)
    table = Product('Table', Color.RED, Size.LARGE)
    house = Product('House', Color.GREEN, Size.MEDIUM)

    products = [chair, table, house]

    pf = ProductFilter()
    print('Red products (old approach):')
    for p in pf.filter_by_color(products, Color.RED):
        print(p.name)
    print('--------------')

    bf = BetterFilter()
    print('Red products (better approach):')
    red_spec = ColorSpecification(Color.RED)
    for p in bf.filter(products, red_spec):
        print(p.name)
    print('--------------')

    print('Medium products (better approach):')
    large_spec = SizeSpecification(Size.MEDIUM)
    for p in bf.filter(products, large_spec):
        print(p.name)
    print('--------------')

    print('Red and Medium products')
    # Both approaches are nice
    # args = (ColorSpecification(Color.RED), SizeSpecification(Size.MEDIUM))
    # red_and_medium_spec = AndSpecification(*args)
    red_and_medium_spec = large_spec & red_spec
    for p in bf.filter(products, red_and_medium_spec):
        print(p.name)
    print('--------------')

    print('Red or Medium products')
    # args = (ColorSpecification(Color.RED), SizeSpecification(Size.MEDIUM))
    # red_or_medium_spec = OrSpecification(*args)
    red_or_medium_spec = large_spec | red_spec
    for p in bf.filter(products, red_or_medium_spec):
        print(p.name)
    print('--------------')
