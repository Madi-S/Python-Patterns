

class BitMap:
    def __init__(self, filename):
        self.filename = filename
        print(f'Loading image from {self.filename}')

    def draw(self):
        print(f'Drawing image {self.filename}')


class LazyBitMap:
    def __init__(self, filename):
        self.filename = filename
        self._bmp = None

    def draw(self):
        if self._bmp is None:
            self._bmp = BitMap(self.filename)
        self._bmp.draw()


def draw_image(image):
    print('About to draw an image')
    image.draw()
    print('Done drawing image')


if __name__ == '__main__':
    # bmp = BitMap('palms.jpg')
    # draw_image(bmp)
    # >>> Loading image from palms.jpg
    # >>> About to draw an image
    # >>> Drawing image palms.jpg
    # >>> Done drawing image
    bmp = LazyBitMap('forest.jpg')
    draw_image(bmp)
    # Does not load image if not needed, only when .draw() is called
    # >>> About to draw an image
    # >>> Loading image from forest.jpg
    # >>> Drawing image forest.jpg
    # >>> Done drawing imag
