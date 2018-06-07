import collections
from typing import Iterable, List


def checkio(numbers: List[int]) -> Iterable[int]:
    counter = collections.Counter(numbers)
    unique_numbers = [number for number, count in counter.items() if count == 1]
    return (number for number in numbers if number not in unique_numbers)
