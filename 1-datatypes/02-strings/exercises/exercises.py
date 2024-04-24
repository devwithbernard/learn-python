"""
Exercises provide by : https://www.w3resource.com/python-exercises/string/
"""

"""
Calculate the length of a string
"""


def calculate_length(string: str):
    """
    Calculate the length of a string
    :param string:
    :return int:
    """
    if string is not None:
        return len(string)
    raise ValueError('Only string is allowed!')


phrase = 'I love programming in python'
print(f"{phrase} ==> {calculate_length(phrase)} characters.")

"""
 Write a Python program to count the number of characters (character frequency) in a string.
"""


def string_frequency(string: str):
    """
    :param string:
    :return dict:
    """
    occurrence = dict()
    for letter in string:
        keys = occurrence.keys()
        if letter in keys:
            occurrence[letter] += 1
        else:
            occurrence[letter] = 1
    return occurrence


print(string_frequency('google.com'))

"""
Write a Python program to get a string made of the first 2 and last 2 characters of a given string.
If the string length is less than 2, return the empty string instead.
"""


def format_str(string: str):
    """
    :param string:
    :return string:
    """
    if len(string) < 2:
        return ''
    # same with: string[:2] + string[len(string) - 2:]
    return string[:2] + string[- 2:]


test_strings = ['w3resource', 'w3', 'w']
for test_string in test_strings:
    print(f"\t{test_string} ==> {format_str(test_string)}")

"""
Write a Python program to get a string from a given string where all occurrences of its first char have been changed
to '$', except the first char itself.
"""


def replace_occurrence_with_dollar_sign(string: str):
    """
        :param string:
        :return string:
    """
    # we can use str.replace(string, '$')
    new_str = string[0]
    for i in range(1, len(string)):
        if string[i] == string[0]:
            new_str += '$'
        else:
            new_str += string[i]
    return new_str


print(replace_occurrence_with_dollar_sign('restart'))

"""
Write a Python program to get a single string from two given strings, separated by a space and swap the first two
characters of each string.
"""


def swap_chars(str1: str, str2: str) -> str:
    """
    :param str1:
    :param str2:
    :return string:
    """
    str1 = str1.strip()
    str2 = str2.strip()
    
    if len(str1) <= 2 and len(str2) <= 2:
        raise ValueError('Length of two strings must be over 3')
    return str2[:2] + str1[-1] + ' ' + str1[:2] + str2[-1]


print(swap_chars('abc', 'xyz'))

"""
Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string
already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
"""


def insert_substring(string: str):
    """
    :param string:
    :return:
    """
    length = len(string)
    
    if length > 2:
        if string[-3:].lower() == 'ing':
            string += 'ly'
        else:
            string += 'ing'
    return string


sample_words = ['abc', 'string', 'eh']
for sample_word in sample_words:
    print(f"{sample_word} ==> {insert_substring(sample_word)}")

"""
Write a Python function that takes a list of words and return the longest word and the length of the longest one.
"""


def longest_word(words: list) -> dict:
    """
    :param words:
    :return dict:
    """
    if len(words) == 0:
        return dict()
    
    length_of_words = [len(word) for word in words]
    dico = {key: value for (key, value) in zip(length_of_words, words)}
    longest_key = max(dico.keys())
    
    return {longest_key: dico[longest_key]}


web_techs = ['python', 'javascript', 'jquery', 'react', 'angular', 'vue']
print(longest_word(web_techs))

"""
Write a Python program to remove the nth index character from a nonempty string
"""


def remove_char(string: str, n: int):
    """
    :param string:
    :param n:
    :return:
    """
    if string.strip() == '':
        raise ValueError('Empty string is not allowed!')
    if len(string.strip()) < n:
        raise Exception(f"{n} must be lower than {string} length")
    return string[:n] + string[n + 1:]


for tech in web_techs:
    print(f"\t{tech} ==> {remove_char(tech, 2)}")

"""
 Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.
"""


def exchange_chars(string: str):
    """
    :param string:
    :return string:
    """
    return (string[-1] + string[1: len(string) - 1] + string[0]).capitalize()


print(exchange_chars('Javascript'))

"""
Write a Python program to count the occurrences of each word in a given sentence.
"""


def count_occurrence(sentence: str) -> dict:
    """
    :param sentence:
    :return:
    """
    dico = {}
    keys = dico.keys()
    words = [word.strip().lower() for word in sentence.split(" ")]
    for word in words:
        if word in keys:
            dico[word] += 1
        else:
            dico[word] = 1
    return dico


sentence = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's
standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a
type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting,
remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem
Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem
Ipsum.
"""

print(count_occurrence(sentence))
