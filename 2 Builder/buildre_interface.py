# HTML elements compilation example

# Bad approach
# text = 'abcd'
# parts = ['<p>', text, '</p>']
# print(''.join(parts))

# words = ['hello', 'world']
# parts = ['<ul>']
# for w in words:
#     parts.append(f'<li>{w}</li>')
# parts.append('</ul>')
# print(''.join(parts))


class HtmlElement:
    indent_size = 4

    def __init__(self, name='', text=''):
        self.name = name
        self.text = text
        self.elements = []

    def __str(self):
        lines = []
        space = ' ' * self.indent_size
        lines.append(f'{space}<{self.name}>')

        if self.text:
            new_space = space * 2
            lines.append(f'{new_space}{self.text}')

        for el in self.elements:
            lines.append(el.__str())

        lines.append(f'{space}</{self.name}>')
        return '\n'.join(lines)

    def __str__(self):
        return self.__str()

    @staticmethod
    def create(name):
        return HtmlBuilder(name)


class HtmlBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = HtmlElement(root_name)

    def add_child(self, child_name, text):
        self.__root.elements.append(
            HtmlElement(child_name, text)
        )

    def add_child_fluent(self, child_name, text):
        self.__root.elements.append(
            HtmlElement(child_name, text)
        )
        return self

    def __str__(self):
        return str(self.__root)


if __name__ == '__main__':
    # builder = HtmlBuilder('ul')
    # builder.add_child('li', 'hello')
    # builder.add_child('li', 'world')

    bulder = HtmlBuilder.create('ul')
    bulder.add_child_fluent('li', 'hello').add_child_fluent('li', 'world')
    print(bulder)
