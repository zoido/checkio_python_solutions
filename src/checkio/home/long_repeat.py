def long_repeat(text: str) -> int:
    if len(text) == 0:
        return 0

    chars = iter(text)
    counter = 1
    max_length = 0
    try:
        previous_char = next(chars)
        while True:
            current_char = next(chars)
            if current_char == previous_char:
                counter += 1
            else:
                max_length = max(max_length, counter)
                counter = 1
            previous_char = current_char
    except StopIteration:
        max_length = max(max_length, counter)
    return max_length
