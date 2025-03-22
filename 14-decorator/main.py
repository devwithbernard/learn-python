def greet_decorator(func):
    def wrapper(name: str) -> None:
        print("Starting...")
        func(name)
        print("Ending....")

    return wrapper


@greet_decorator
def hello(name: str) -> None:
    print(f"Hello {name}")


if __name__ == "__main__":
    hello("Jack")
