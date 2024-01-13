from enum import Enum, auto


class Token:
    class Type(Enum):
        INTEGER = auto()
        PLUS = auto()
        MINUS = auto()
        LPAREN = auto()
        RPAREN = auto()

    def __init__(self, token_type, text):
        self.text = text
        self.type = token_type

    def __repr__(self):
        return f'`{self.text}`'


def lex(input_str):
    result = []

    i = 0
    while i < len(input_str):
        if input_str[i] == '+':
            result.append(Token(Token.Type.PLUS, '+'))
        elif input_str[i] == '-':
            result.append(Token(Token.Type.MINUS, '-'))
        elif input_str[i] == '(':
            result.append(Token(Token.Type.LPAREN, '('))
        elif input_str[i] == ')':
            result.append(Token(Token.Type.RPAREN, ')'))
        elif input_str[i].isdigit():
            digits = [input_str[i], ]
            for j in range(i + 1, len(input_str)):
                if input_str[j].isdigit():
                    digits.append(input_str[j])
                    i += 1
                else:
                    digits = ''.join(digits)
                    digit_token = Token(Token.Type.INTEGER, digits)
                    result.append(digit_token)
                    break
        i += 1

    return result


class Integer:
    def __init__(self, value):
        self.value = value


class BinaryExpression:
    class Type(Enum):
        ADDITION = auto()
        SUBTRACTION = auto()

    def __init__(self):
        self.type = None
        self.left = None
        self.right = None

    @property
    def value(self):
        if self.type == self.Type.ADDITION:
            return self.left.value + self.right.value
        elif self.type == self.Type.SUBTRACTION:
            return self.left.value - self.right.value


def parse(tokens):
    result = BinaryExpression()
    has_lhs = False
    i = 0
    while i < len(tokens):
        token = tokens[i]

        if token.type == Token.Type.INTEGER:
            integer = Integer(int(token.text))
            if not has_lhs:
                result.left = integer
                has_lhs = True
            else:
                result.right = integer

        elif token.type == Token.Type.PLUS:
            result.type = BinaryExpression.Type.ADDITION
        elif token.type == Token.Type.MINUS:
            result.type = BinaryExpression.Type.SUBTRACTION
        elif token.type == Token.Type.LPAREN:
            j = i
            while j < len(tokens):
                if tokens[j].type == Token.Type.RPAREN:
                    break
                j += 1
            subexpression = tokens[i + 1:j]
            element = parse(subexpression)
            if not has_lhs:
                result.left = element
                has_lhs = True
            else:
                result.right = element
            i = j
        i += 1

    return result


def calc(input_str):
    tokens = lex(input_str)
    print(tokens)

    parsed = parse(tokens)
    print(f'{input_str} = {parsed.value}')


if __name__ == '__main__':
    calc('(13 + 4) - (12 + 1)')
