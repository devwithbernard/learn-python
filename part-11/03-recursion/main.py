"""
Recursion
"""

# A function calls itself
def hello(name: str) -> None:
    print("Hello", name)

def hello_many_times(name: str, times: int) -> None:
    for i in range(times):
        hello(name)


hello_many_times("Bernard", 5)