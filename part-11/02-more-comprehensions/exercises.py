# TODO: Filter forbidden
def filter_forbidden(text: str, forbidden: str):
    def filter_character(word):
        return "".join([character for character in word if character.lower() not in forbidden.lower()])

    return " ".join([filter_character(word) for word in text.split(" ")])

sentence = "Once! upon, a time: there was a python!??!?!"
filtered = filter_forbidden(sentence, "!?:,.")
print(filtered)