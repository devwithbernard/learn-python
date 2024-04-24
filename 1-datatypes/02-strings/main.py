message = 'Hello world'
longText = ''
for word in message.split(' '):
    longText += word + '\n'

print(longText)

phrase = "I love programming in python"
phrase_with_separator = ''
iterable = phrase.split(' ')
for index, word in enumerate(iterable):
    if index + 1 != len(iterable):
        phrase_with_separator += word + '-'
    else:
        phrase_with_separator += word

print('New phrase:', phrase_with_separator)