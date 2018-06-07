from typing import Sequence


def index_power(array: Sequence[int], index: int) -> int:
    try:
        return array[index] ** index
    except IndexError:
        return -1
