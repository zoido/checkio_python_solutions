import functools
import operator


def checkio(number: int):
    return functools.reduce(
        operator.mul, (int(digit) for digit in str(number) if digit != "0")
    )
