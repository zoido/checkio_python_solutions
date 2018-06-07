from typing import List


def checkio(numbers: List[int]) -> int:
    if not numbers:
        return 0
    return sum(numbers[::2]) * numbers[-1]
