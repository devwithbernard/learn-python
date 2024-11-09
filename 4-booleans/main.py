"""
Working with booleans
"""

print(9 > 10)
print(20 == 10)
print(2 > 1)

f_values: list = [0, {}, [], set(), '', False]
falsy_values: list = [bool(f) for f in f_values]
print(falsy_values)

number1: int = 10
number2: int = 20

if number2 > number1:
	print(f"{number2} > {number1}")
else:
	print(f"{number2} < {number1}")


# Case that object instance evaluates to False
class Obj:
	def __len__(self):
		return 0


print(bool(Obj()))  # False


# Function can return a Boolean
def is_adult(age: int) -> bool:
	"""
	Check if a person is an adult
	:param age: The age of the person
	:return: True if the person is an adult (18 or older), False otherwise
	"""
	return age >= 18


print(is_adult(28))