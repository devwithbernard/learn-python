"""
Learn more list features
"""

# TODO: Reversed list

def reversed_list(names: list[str]) -> list[str] | None:
    if not names:
        return None

    if len(names) == 0:
        return []

    index = len(names) - 1
    new_list: list[str] = []

    while index >= 0:
        new_list.append(names[index])
        index -= 1

    return new_list


name_list = ["Steve", "Jean", "Katherine", "Paul"]
reversed_lst = reversed_list(name_list)
print(reversed_lst)
