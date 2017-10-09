from typing import Iterable, List


def checkio(numbers: Iterable[int]) -> List[int]:
    return list(sorted(numbers, key=abs))
