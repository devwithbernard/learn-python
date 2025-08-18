"""
Course Statistics
"""

from urllib import request
import json


def get_data(url: str) -> list[tuple]:
    with request.urlopen(url) as r:
        data = json.loads(r.read())
        format_data = []

        for item in data:
            d = (item['fullName'], item['name'], item['year'], sum(item['exercises']))
            format_data.append(d)

        return format_data


def get_active_courses():
    courses = get_data("https://studies.cs.helsinki.fi/stats-mock/api/courses")

    names = tuple([item[1] for item in courses])


def retrieve_course(name: str) -> dict | None:
    with request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{name}/stats") as r:
        data: dict = json.loads(r.read())

        if not data:
            print("Data doesn't exist")
            return None

        # Values
        weeks = len(data.keys())
        students = max([data[course]['students'] for course in data])
        hours = sum([data[course]['hour_total'] for course in data])
        hours_average = round(hours / students)
        exercises = sum([data[course]['exercise_total'] for course in data])
        exercises_average = round(exercises / students)

        course_stats = {
            "weeks": weeks,
            "students": students,
            "hours": hours,
            "hours_average": hours_average,
            "exercises": exercises,
            "exercises_average": exercises_average
        }

        return course_stats


course_stats = retrieve_course("docker2019")
print(course_stats)