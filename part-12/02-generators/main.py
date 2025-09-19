def return_item(items: list[int]):
    i = 0
    while i < len(items):
        yield items[i]
        i += 1


item = return_item([1, 2, 3, 4])
try:
    print(next(item))
    print(next(item))
    print(next(item))
    print(next(item))
    print(next(item))
except StopIteration:
    print("End of iteration")