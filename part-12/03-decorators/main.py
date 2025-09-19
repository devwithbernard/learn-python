"""
Decorators
"""

def decorator(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")
    return wrapper

@decorator
def greet():
    print("Hello word")

greet()

# Decorator with parameters
def decorator_name(function):
    def wrapper(*args, **kwargs):
        print("Before execution")
        result = function(*args, **kwargs)
        print("After execution")
        return result
    return wrapper


@decorator_name
def add(a, b):
    return a + b


print(add(10, 5))