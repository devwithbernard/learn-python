from compledtecourse import CompletedCourse
from student import Student
from course import Course
from player import Player
from team import Team

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

    # A list of objects as an attribute of an object
    ca = Team("Campus Allstars")
    ca.add_player(Player("Eric", 10))
    ca.add_player(Player("Emily", 22))
    ca.add_player(Player("Andy", 1))
    ca.summary()

    # None: a reference to nothing
    print(ca.find_player("Andy"))

    print(ca.find_player("Mark"))

    ca = Team("Campus UIA")
    ca.add_player(Player("Eric", 10))

    player = ca.find_player("Charlie")
    if player is not None:
        print(F"Goals by charlie: {player.goals}")
    else:
        print("Charlies doesn't play in campus")


if __name__ == '__main__':
    main()
