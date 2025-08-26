from compledtecourse import CompletedCourse
from student import Student
from course import Course


def main() -> None:
    # List of students
    students: list[Student] = [Student("Ollie", "1234", 10), Student("Peter", "3210", 23), Student("Lena", "9999", 43),
                               Student("Tina", "3333", 8)]

    # Create a course named Introduction to Programming
    itp = Course("Introduction to Programming", "itp1", 5)

    # Add completed courses for each student, with grade 3 for all
    completed = []
    for student in students:
        completed.append(CompletedCourse(student, itp, 3))

    # Print out the name of the student for each completed course
    for course in completed:
        print(course.student.name)


if __name__ == '__main__':
    main()
