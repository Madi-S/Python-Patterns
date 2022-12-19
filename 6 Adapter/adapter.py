# Adapter pattern is used to connect various incompatible classes/interfaces together
# So that, adapter makes one interface compatible with another


# Given API (cannot be modified)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def draw_point(point):
    print('.', end='')


# Intermediate adapter to adapt external api to ours
class LineToPointAdapter(list):
    count = 0

    def __init__(self, line):
        super().__init__()
        self.count += 1

        print(f'{self.count}: Generating points for line '
              f'[{line.start.x},{line.start.y}]→'
              f'[{line.end.x},{line.end.y}]')

        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = min(line.start.y, line.end.y)
        bottom = min(line.start.y, line.end.y)

        # Rearranging points order so that a correct line would appear
        if right - left == 0:
            for y in range(top, bottom):
                self.append(Point(left, y))
        elif line.end.y - line.start.y == 0:
            for x in range(left, right):
                self.append(Point(x, top))


# Our API
class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Rectangle(list):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.append(Line(Point(x, y), Point(x + width, y)))
        self.append(Line(Point(x, y), Point(x, y + height)))
        self.append(Line(Point(x + width, y), Point(x + width, y + height)))
        self.append(Line(Point(x, y + height), Point(x + width, y + height)))


def draw_rectangles(rectangles):
    print('\n\nDrawing rectangles\n')
    for rectangle in rectangles:
        for line in rectangle:
            adapter = LineToPointAdapter(line)
            for p in adapter:
                draw_point(p)


if __name__ == '__main__':
    rectangles = [
        Rectangle(1, 1, 10, 10),
        Rectangle(5, 5, 6, 6),
    ]
    draw_rectangles(rectangles)
    draw_rectangles(rectangles)
