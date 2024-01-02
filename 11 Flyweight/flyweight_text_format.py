

class FormattedText:
    def __init__(self, plain_text):
        self.plain_text = plain_text
        self.caps = [False for _ in range(len(plain_text))]

    def capitalize(self, start, end):
        for i in range(start, end):
            self.caps[i] = True

    def __str__(self):
        result = []
        for i in range(len(self.plain_text)):
            c = self.plain_text[i]
            result.append(
                c.upper() if self.caps[i] else c
            )
        return ''.join(result)


# Flyweight applied
class BetterFormattedText:
    def __init__(self, plain_text):
        self.plain_text = plain_text
        self.formatting = []

    class TextRange:
        def __init__(self, start, end, capitalize=False):
            self.start = start
            self.end = end
            self.capitalize = capitalize

        def covers(self, position):
            return self.start <= position <= self.end

    def get_range(self, start, end):
        range = self.TextRange(start, end)
        self.formatting.append(range)
        return range

    def __str__(self):
        result = []
        for i in range(len(self.plain_text)):
            c = self.plain_text[i]
            for text_range in self.formatting:
                if text_range.covers(i) and text_range.capitalize:
                    c = c.upper()
            result.append(c)

        return ''.join(result)


if __name__ == '__main__':
    text = 'This is a brave new world'
    ft = FormattedText(text)
    ft.capitalize(10, 15)
    print(ft)
    # >>> This is a BRAVE new world

    bft = BetterFormattedText(text)
    bft.get_range(16, 19).capitalize = True
    print(bft)
    # >>> This is a brave NEW world
