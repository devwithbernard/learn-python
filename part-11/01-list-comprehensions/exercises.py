"""
List comprehensions: Exercises
"""
import math

# TODO: Square roots

def square_roots(numbers: list[float]) -> list[float]:
    if not numbers:
        raise ValueError(f'{numbers} is not in correct format')
    return [math.sqrt(x) for x in numbers]


lines = square_roots([1,2,3,4])
for line in lines:
    print(line)

# TODO: Rows of stars
def rows_of_stars(numbers: list[int]) -> list[str]:
    if not numbers:
        raise ValueError(f'{numbers} is not in correct format')
    return [ '*' * x for x in numbers]

rows = rows_of_stars([1,2,3,4])
for row in rows:
    print(row)

print()

rows = rows_of_stars([4, 3, 2, 1, 10])
for row in rows:
    print(row)


# TODO: Best exam result
class ExamResult:
    def __init__(self, name: str, grade1: int, grade2: int, grade3: int) -> None:
        self.name = name
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3

    @property
    def grades(self):
        return [self.grade1, self.grade2, self.grade3]


def best_results(results: list[ExamResult]) -> dict[str, list[int]]:
    max_result = max(results, key=lambda result: sum(result.grades))
    return {max_result.name: max_result.grades}


result1 = ExamResult("Peter",5,3,4)
result2 = ExamResult("Pippa",3,4,1)
result3 = ExamResult("Paul",2,1,3)
results = [result1, result2, result3]
print(best_results(results))

# TODO: Lengths

def lengths(lists: list[list]):
    return [len(item) for item in lists]

lists = [[1,2,3,4,5], [324, -1, 31, 7],[]]
print(lengths(lists))

# TODO: Remove smaller than

def remove_smaller_than(numbers: list, limit: int):
    return [number for number in numbers if number >= limit]

numbers = [1,65, 32, -6, 9, 11]
print(remove_smaller_than(numbers, 10))

print(remove_smaller_than([-4, 7, 8, -100], 0))

# TODO: Begin with a vowel

def begin_with_vowel(words: list[str]) -> list[str]:
    VOWELS = ('a', 'e', 'i', 'o', 'u' , 'y')
    return [word for word in words if word.lower()[0] in VOWELS]

word_list = ["automobile","motorbike","Animal","cat","Dog","APPLE","orange"]
for vowelled in begin_with_vowel(word_list):
    print(vowelled)