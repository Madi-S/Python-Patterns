# Visitor is a template, in which
# every component (visitor) is allowed
# to go through the all hierarchy of inheritance
# Its realization is defined in method `.visit()`
# along the all hierarchy of classes


class DoubleExpression:
    def __init__(self, value):
        self.value = value

    def print(self, buffer):
        buffer.append(str(self.value))

    def eval(self):
        return self.value


class AdditionExpression:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def print(self, buffer):
        buffer.append('( ')
        self.left.print(buffer)
        buffer.append(' + ')
        self.right.print(buffer)
        buffer.append(' )')

    def eval(self):
        return self.left.eval() + self.right.eval()


if __name__ == '__main__':
    # 1 + (2 + 3)
    e = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )
    buffer = []
    e.print(buffer)
    print(''.join(buffer), '=', e.eval())
    # >>> ( 1 + ( 2 + 3 ) ) = 6