import os

courses = ["History", "French", "Math"]

for course in courses:
    current_path = os.path.join(os.getcwd(), course)
    if os.path.exists(current_path):
        with open(os.path.join(current_path, course.join('.py')), 'a') as f:
            os.utime(os.path.join(current_path, course.join('.py')), None)
    else:
        os.mkdir(os.path.join(os.getcwd(), course))
