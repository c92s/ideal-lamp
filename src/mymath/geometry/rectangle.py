from geometry.point import Point


class Rectangle:
    def __init__(self, upper_left: Point, lower_right: Point):
        self.upper_left = upper_left
        self.upper_right = Point(lower_right.x, upper_left.y)
        self.lower_right = lower_right
        self.lower_left = Point(upper_left.x, lower_right.y)

    def __repr__(self) -> str:
        return f"Rectangle({self.upper_left}, {self.lower_right})"
