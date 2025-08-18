import csv
import datetime
import pprint


def get_hour_mins(hour_min: str) -> datetime.time:
    hours_mins = hour_min.split(":")
    hour = int(hours_mins[0])
    mins = int(hours_mins[1])
    return datetime.time(hour, mins)


def get_start_time_per_student(filename: str) -> dict[str, datetime.time]:
    with open(filename) as file:
        csv_reader = csv.reader(file, delimiter=";")
        student_time = {}

        for row in csv_reader:
            if row[0] not in student_time:
                start_time = get_hour_mins(row[1])
                student_time[row[0]] = start_time

        return student_time


def format_submissions(filename: str):
    students = {}

    with open(filename) as file:
        csv_reader = csv.reader(file, delimiter=";")

        for row in csv_reader:
            st_data = {
                "task": int(row[1]),
                "points": int(row[2]),
                "hour_mins": get_hour_mins(row[3])
            }

            if row[0] not in students:
                students[row[0]] = []
                students[row[0]].append(st_data)
            else:
                students[row[0]].append(st_data)

        for name, submissions in students.items():
            submissions.sort(key=lambda submission: submission['task'])

    return students


def max_submission_time_per_student(submissions: dict):
    max_submissions = {}

    for name, values in submissions.items():
        max_sub_per_std = max([val['hour_mins'] for val in values])
        max_submissions[name] = max_sub_per_std

    return max_submissions


def who_cheated(start_times, max_sub_times) -> list[str]:
    MAX_HOUR_IN_SECONDS = 3 * 3600

    names: list[str] = []

    for name, hour in max_sub_times.items():
        dt1 = datetime.datetime.combine(datetime.date.today(), hour)
        dt2 = datetime.datetime.combine(datetime.date.today(), start_times[name])

        diff = dt1 - dt2

        if diff.total_seconds() > MAX_HOUR_IN_SECONDS:
            names.append(name)

    return names


def main() -> None:
    student_start_times = get_start_time_per_student("files/start_time.csv")
    submissions = format_submissions("files/submissions.csv")
    max_sub_per_students = max_submission_time_per_student(submissions)

    names = who_cheated(student_start_times, max_sub_per_students)

    print("Cheater of exam:")
    for name in names:
        print(name)


if __name__ == "__main__":
    main()
