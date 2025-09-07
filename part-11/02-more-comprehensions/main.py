"""
More comprehensions
"""

# Comprehensions with strings

name = "Peter Python"

uppercased = [character.upper() for character in name]
print(uppercased)

# Replace vowels with *
test_string = "Hello there, this is a test!"

test_string_after_replacing = ['*' if character.lower() in 'aeiouy' else character for character in test_string]
new_string = "".join(test_string_after_replacing)

print(new_string)

# Text with no initials
sentence = "Sheila keeps on selling seashells on the seashore"
text_with_no_initials = " ".join( word[1:] for word in sentence.split(" "))
print(text_with_no_initials)