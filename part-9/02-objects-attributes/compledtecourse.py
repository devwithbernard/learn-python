from student import Student
from course import Course


class CompletedCourse:
    def __init__(self, student: Student, course: Course, grade: int) -> None:
        self.student = student
        self.course = course
        self.grade = grade
