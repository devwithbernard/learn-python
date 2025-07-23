# TODO: Function definition
def greeting():
    print("Hello everyone!")


greeting()


# TODO: Function arguments
def hello(target):
    print("Hello", target)


hello("Emily")
hello("World!")


# Exercise
# TODO: Seven Brothers
def display_name(name: str) -> None:
    print(name)


names: list[str] = ['Aapo', 'Eero', 'Juhani', 'Lauri',
                    'Simeoni', 'Timo', 'Tuomas']

for name in names:
    display_name(name)

# TODO: Find the best students
students: list[dict[str, object]] = [
    {'name': 'Aapo', 'class': '6ème', 'notes': [14.7, 15.2, 13.1, 17.4]},
    {'name': 'Eero', 'class': '6ème', 'notes': [18.6, 11.3, 12.5, 16.8]},
    {'name': 'Juhani', 'class': '6ème', 'notes': [15.0, 13.9, 14.2, 17.5]},
    {'name': 'Lauri', 'class': '6ème', 'notes': [12.6, 16.1, 14.8, 18.9]},
    {'name': 'Simeoni', 'class': '6ème', 'notes': [11.7, 17.3, 13.4, 19.1]},
    {'name': 'Timo', 'class': '5ème', 'notes': [14.1, 15.6, 16.2, 13.3]},
    {'name': 'Tuomas', 'class': '5ème', 'notes': [13.0, 12.4, 17.8, 18.2]},
    {'name': 'Mika', 'class': '5ème', 'notes': [16.5, 14.9, 15.7, 12.8]},
    {'name': 'Oskari', 'class': '5ème', 'notes': [12.3, 11.6, 14.0, 17.2]},
    {'name': 'Aleksi', 'class': '5ème', 'notes': [18.0, 13.2, 15.4, 16.9]},
    {'name': 'Elias', 'class': '4ème', 'notes': [11.4, 13.1, 16.7, 14.3]},
    {'name': 'Ville', 'class': '4ème', 'notes': [12.2, 17.6, 13.9, 18.1]},
    {'name': 'Onni', 'class': '4ème', 'notes': [14.5, 15.8, 13.6, 17.0]},
    {'name': 'Anton', 'class': '4ème', 'notes': [16.3, 12.5, 18.4, 14.6]},
    {'name': 'Leo', 'class': '4ème', 'notes': [13.8, 14.4, 12.1, 15.9]},
    {'name': 'Oliver', 'class': '3ème', 'notes': [17.3, 15.1, 14.0, 13.2]},
    {'name': 'Otto', 'class': '3ème', 'notes': [11.9, 18.6, 12.7, 16.5]},
    {'name': 'Eemil', 'class': '3ème', 'notes': [13.5, 16.0, 14.9, 12.6]},
    {'name': 'Samuel', 'class': '3ème', 'notes': [12.8, 17.1, 13.3, 15.5]},
    {'name': 'Luka', 'class': '3ème', 'notes': [14.6, 12.9, 15.2, 16.4]},
]


# Organize students per class
def get_students_per_class(students: list[dict[str, str, object]]) -> dict[str, object]:
    classes: dict[str, list] = {}

    for student in students:
        std_class = student['class']
        new_student: dict[str, object] = {'name': student.get('name'),
                                          'notes': student.get('notes')}
        if student['class'] in classes:
            classes[std_class].append(new_student)
        else:
            classes[std_class] = []
            classes[std_class].append(new_student)

    return classes


def find_best_student_per_class(stds: list) -> dict:
    return max(stds, key=lambda std: round(sum(std['notes']) / len(std['notes']), 2))


def calculate_mean(notes: list[float]) -> float:
    return round(sum(notes) / len(notes), 2)


def format_student(student) -> str:
    mean = calculate_mean(student['notes'])
    notes_str = ', '.join([ str(note) for note in student['notes']])

    return f"""
    Name: {student['name']}
    Notes: {notes_str}
    mean: {mean}/20
    """


classes = get_students_per_class(students)

for level, students in classes.items():
    print(f"-------------- {level} ----------------")
    best_student = find_best_student_per_class(students)
    print(format_student(best_student))
