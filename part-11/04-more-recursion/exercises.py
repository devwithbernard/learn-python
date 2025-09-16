"""
Exercises : More recursion
"""


# TODO: Bosses and Subordinates

class Employee:
    def __init__(self, name: str):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, subordinate: 'Employee'):
        self.subordinates.append(subordinate)


def count_subordinates(employee: Employee) -> int:
    if len(employee.subordinates) == 0:
        return 0

    count = 0

    for subordinate in employee.subordinates:
        count += 1 + count_subordinates(subordinate)

    return count


t1 = Employee("Sally")
t2 = Employee("Eric")
t3 = Employee("Matthew")
t4 = Employee("Emily")
t5 = Employee("Adele")
t6 = Employee("Claire")
t1.add_subordinate(t4)
t1.add_subordinate(t6)
t4.add_subordinate(t2)
t4.add_subordinate(t3)
t4.add_subordinate(t5)
print(count_subordinates(t1))
print(count_subordinates(t4))
print(count_subordinates(t5))
