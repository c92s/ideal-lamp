from .geometry.point import Point
from .geometry.rectangle import Rectangle

class RectangleService:
    def create(self, x1, y1, x2, y2):
        return Rectangle(Point(x1, y1), Point(x2, y2))
    
    