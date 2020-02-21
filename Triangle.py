from polygon import polygon
from shape import shape

class Triangle (polygon, shape):
    def area (self):
        return self.get_width() *self.get_height() / 2