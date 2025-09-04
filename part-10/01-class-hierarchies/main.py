"""
Class hierarchies
"""

class Person:

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email

    def update_email_domain(self, new_domain: str) -> None:
        old_domain = self.email.split("@")[1]
        self.email = self.email.replace(old_domain, new_domain)

# Inheritance
class Student(Person):

    def __init__(self, name: str, student_id: str, email: str, credit: int = 0) -> None:
        super().__init__(name, email)
        self.student_id = student_id
        self.credits = credit


class Teacher(Person):

    def __init__(self, name: str, email: str, room: str, teaching_years: int) -> None:
        super().__init__(name, email)
        self.room = room
        self.teaching_years = teaching_years



saul = Student("Saul Student", "1234", "saul@example.com", 0)
saul.update_email_domain("example.edu")
print(saul.email)

tara = Teacher("Tara Teacher", "tara@example.fi", "A123", 2)
tara.update_email_domain("example.ex")
print(tara.email)