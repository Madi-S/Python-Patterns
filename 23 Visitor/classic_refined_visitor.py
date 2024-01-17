# taken from https://tavianator.com/the-visitor-pattern-in-python


def _qualname(obj):
    '''Get the fully-qualified name of an object (including module).'''
    return obj.__module__ + '.' + obj.__qualname__


def _declaring_class(obj):
    '''Get the name of the class that declared an object.'''
    name = _qualname(obj)
    return name[:name.rfind('.')]


# Stores the actual visitor methods
_methods = {}


# Delegating visitor implementation
def _visitor_impl(self, arg):
    '''Actual visitor method implementation.'''
    method = _methods[(_qualname(type(self)), type(arg))]
    return method(self, arg)


# The actual @visitor decorator
def visitor(arg_type):
    '''Decorator that creates a visitor method.'''

    def decorator(fn):
        declaring_class = _declaring_class(fn)
        _methods[(declaring_class, arg_type)] = fn

        # Replace all decorated methods with _visitor_impl
        return _visitor_impl

    return decorator


# ↑↑↑ LIBRARY CODE ↑↑↑


class DoubleExpression:
    def __init__(self, value):
        self.value = value


class AdditionExpression:
    def __init__(self, left, right):
        self.left = left
        self.right = right


# class SubtractionExpression:
#     def __init__(self, left, right):
#         self.left = left
#         self.right = right


class ExpressionPrinter:
    def __init__(self):
        self.buffer = []

    @visitor(DoubleExpression)
    def visit(self, e):
        self.buffer.append(str(e.value))

    @visitor(AdditionExpression)
    def visit(self, e):
        self.buffer.append('( ')
        self.visit(e.left)
        self.buffer.append(' + ')
        self.visit(e.right)
        self.buffer.append(' )')

    def __str__(self):
        return ''.join(self.buffer)


class ExpressionEvaluator:
    def __init__(self):
        self.value = None

    @visitor(DoubleExpression)
    def visit(self, e):
        self.value = e.value

    @visitor(AdditionExpression)
    def visit(self, e):
        self.visit(e.left)
        temp = self.value
        self.visit(e.right)
        self.value += temp


if __name__ == '__main__':
    # 1 + (2 + 3)
    e = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )
    printer = ExpressionPrinter()
    printer.visit(e)

    evaluator = ExpressionEvaluator()
    evaluator.visit(e)

    print(f'{printer} = {evaluator.value}')
