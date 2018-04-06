import operator


def find_extreme(compare_operator, *args, **kwargs):
    key = kwargs.get("key", lambda x: x)
    items = iter(args if len(args) > 1 else args[0])
    try:
        smallest_item = next(items)
        while True:
            next_item = next(items)
            if compare_operator(key(next_item), key(smallest_item)):
                smallest_item = next_item
    except StopIteration:
        pass

    return smallest_item


def min(*args, **kwargs):  # noqa: A001 (needed by definition)
    return find_extreme(operator.lt, *args, **kwargs)


def max(*args, **kwargs):  # noqa: A001 (needed by definition)
    return find_extreme(operator.gt, *args, **kwargs)
