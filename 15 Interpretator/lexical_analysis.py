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
        self.token_type = token_type

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


def calc(input_str):
    tokens = lex(input_str)
    print(tokens)


if __name__ == '__main__':
    calc('(13+4)-(12+1)')
