def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("You've reached the end of the iteration")
# print(first(['Lawrence', 'Abiodun', 'Emmanuel']))
