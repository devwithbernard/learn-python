"""
Reading data from a file
"""

# Read the contents of a file

with open("files/example.txt") as file:
    contents = file.read()
    print(contents)

# Going through the contents of a file

with open("files/example.txt") as f:
    count_line = 0

    for line in f:
        count_line += 1
        print(f"Line {count_line}:", line.replace("\n", ""))


# Reading CSV files
def format(titles: tuple[str, ...], parts: list[str]) -> dict[str, str]:
    new_dict = {}

    for i in range(len(titles)):
        if titles[i] in ('id', 'work_year', 'remote_ratio'):
            new_dict[titles[i]] = int(parts[i])
        elif titles[i] in ('salary', 'salary_in_usd'):
            new_dict[titles[i]] = float(parts[i])
        else:
            new_dict[titles[i]] = parts[i]

    return new_dict


def get_salaries(employees: dict) -> list[float]:
    salaries: list[float] = [employee['salary'] for employee in employees]

    return salaries


def mean_salaries(salaries: list[float]) -> int:
    return round(sum(salaries) // len(salaries))


titles: tuple[str, ...] = tuple()
employees: list[dict] = []

with open("files/ds_salaries.csv") as file:
    first_line = file.readline()
    titles = tuple(first_line.replace("\n", "").split(","))

    for line in file:
        line = line.replace("\n", "")
        parts: list[str] = line.split(",")
        employees.append(format(titles, parts))


def get_employees_per_job(employees: list[dict]) -> dict[str, list[dict]]:
    category: dict = {}

    for employee in employees:
        job_title = employee['job_title'].lower()
        if job_title not in category:
            category[job_title] = []
            category[job_title].append(employee)
        else:
            category[job_title].append(employee)

    return category


# Get mean salary
mean_salary = mean_salaries(get_salaries(employees))

# Employees that gain more than mean salary

paid_employees = [employee for employee in employees if employee['salary'] >= mean_salary]

for paid_employee in paid_employees:
    print(f"{paid_employee['id']}. {paid_employee['experience_level']} => {paid_employee['salary']}")

# Employee per job
employees_per_job = get_employees_per_job(employees)

for emp, values in employees_per_job.items():
    print(f"{emp.title()} -> {len(values)} employee{'s' if len(values) > 1 else ''}")


# Reading file the right way

def reading_file_right_way(file) -> list[dict]:
    persons = []

    with open(file) as f:
        for line in f:
            line = line.replace("\n", "").split(";")
            person = {"name": line[0], "age": int(line[1]), "town": line[2]}
            persons.append(person)

    return persons



def find_oldest_person(persons: list[dict]) -> dict:
    oldest_person = persons[0]

    for person in persons[1:]:
        if person['age'] > oldest_person['age']:
            oldest_person = person

    return oldest_person


persons = reading_file_right_way("files/people.csv")
oldest_person = find_oldest_person(persons)

print(oldest_person)

