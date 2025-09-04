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

# Second use case: Default values of parameters

class Student:

    def __init__(self, name: str, student_number: str, credits: int = 0, notes: str = "", completed_courses = None) -> \
            None:
        self.name = name

        if len(student_number) < 5:
            raise ValueError('A student number should have at least five characters')


        self.__student_number = student_number
        self.credits = credits
        self.__notes = notes
        self.completed_courses = completed_courses

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if name != "":
            self.__name = name
        else:
            raise ValueError("The name cannot be an empty string")

    @property
    def student_number(self) -> str:
        return self.__student_number

    @property
    def credits(self) -> int:
        return self.__credits

    @credits.setter
    def credits(self, op: int) -> None:
        if op >= 0:
            self.__credits = op
        else:
            raise ValueError('The number of study credits cannot be below zero')

    @property
    def notes(self) -> str:
        return self.__notes

    @notes.setter
    def notes(self, notes: str) -> None:
        self.__notes = notes

    @property
    def completed_courses(self) -> list | None:
        return self.__completed_courses

    @completed_courses.setter
    def completed_courses(self, completed_courses) -> None:
        if completed_courses is None:
            self.__completed_courses = []
        else:
            self.__completed_courses = completed_courses

    def add_course(self, course: str) -> None:
        self.completed_courses.append(course)

    def summary(self):
        print(f"Student {self.__name} ({self.student_number}):")
        print(f"- credits: {self.__credits}")

        if self.notes:
            print(f"- notes: {self.notes}")
        else:
            print("- notes: no notes available")
        if self.completed_courses:
            print(f"- completed courses: {', '.join(self.completed_courses)}")


# Passing only the name and the student number as arguments to the constructor
student1 = Student("Sally Student", "12345")
student1.add_course("ACiP")
student1.add_course("ItP")
student1.summary()


# Passing the name, the student number and the number of study credits
student2 = Student("Sassy Student", "54321", 25)
student2.summary()

# Passing values for all the parameters
student3 = Student("Saul Student", "99999", 140, "extra time in exam")
student3.summary()

# Passing a value for notes, but not for study credits
# NB: the parameter must be named now that the arguments are not in order
student4 = Student("Sandy Student", "98765", notes="absent in academic year 20-21")
student4.summary()