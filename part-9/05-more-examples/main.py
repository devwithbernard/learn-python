"""
More examples with classes : use case
"""

import math

# First use case
"""
A Point is a model for a point in two-dimensional space
attributes: x : float, y: float
"""


class Point:
    """The class represents a point in two-dimensional space"""

    def __init__(self, x: float, y: float) -> None:
        """These attributes are public because any value
        of float or int type is acceptable for x and y"""
        self.x = x
        self.y = y

    # This class method returns a new Point at origo (0, 0)
    @classmethod
    def origo(cls) -> "Point":
        return Point(0, 0)

    # This class method creates a new Point based on an existing Point
    # The original Point can be mirrored on either or both of the x and y axes
    # For example, the Point(1, 3) mirrored on the x-axis is (1, -3)
    @classmethod
    def mirrored(cls, point: "Point", mirror_x: bool, mirror_y: bool) -> "Point":
        x = point.x
        y = point.y

        if mirror_x:
            y = -y
        if mirror_y:
            x = -x

        return Point(x, y)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


class Line:
    """ The class represents a line segment in two-dimensional space """

    def __init__(self, beginning: Point, end: Point) -> None:
        self.beginning = beginning
        self.end = end

    # This method uses the Pythagorean theorem to calculate the length of the line segement
    def length(self) -> float:
        sum_of_squares = (self.end.x - self.beginning.x) ** 2 + (self.end.y - self.beginning.y) ** 2
        return math.sqrt(sum_of_squares)

    # This method returns the Point in the middle of the line segment
    def centre(self) -> Point:
        centre_x = (self.beginning.x + self.end.x) / 2
        centre_y = (self.beginning.y + self.end.y) / 2
        return Point(centre_x, centre_y)

    def __str__(self) -> str:
        return f"{self.beginning} ... {self.end}"



point: Point = Point(7, 8)
origo = Point.origo()

print(origo)

mirrored_point = Point.mirrored(point, False, True)

line = Line(point, mirrored_point)

print("Length of line:", line.length())
print("Centre of line:", line.centre())
print("Line:", line)