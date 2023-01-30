"""
    Our frames
"""


class Frame:
    def __init__(self, text=None, background=None):
        self._text = text
        self._background = background
        self.img = None

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, value):
        self._background = value

    def make_frame(self):
        from PIL import Image
        from PIL import ImageDraw

        self.img = Image.open(self._background)
        draw = ImageDraw.Draw(self.img)
        draw.text((0, 0), self._text, (0, 255, 255))

    def save(self, filename="sample.png"):
        self.img.save(filename)
