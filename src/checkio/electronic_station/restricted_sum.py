def checkio(numbers):
    length = len(numbers)

    if length == 0:
        return 0

    if length == 1:
        return numbers[0]
    else:
        return numbers[-1] + checkio(numbers[:-1])
