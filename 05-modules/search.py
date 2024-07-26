
print('Import Search module')

BASE_LANGUAGE = 'Python'


def find_index(to_search: list, target) -> int:
    """
    Find the index of the value in the sequence
    """
    for index, value in enumerate(to_search):
        if value == target:
            return index

    return -1
