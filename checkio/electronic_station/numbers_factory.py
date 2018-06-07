from typing import Generator


def find_factors(number: int) -> Generator[int, None, None]:
    n = int(number)
    while n > 1:
        divided = False
        for digit in range(9, 1, -1):
            if n % digit == 0:
                n //= digit
                divided = True
                yield digit
                break
        if n < 10:
            yield n
            break
        if not divided:
            raise ValueError("No reasonable factors can be found.")


def checkio(number: int) -> int:
    try:
        factors = sorted(find_factors(number))
        return int("".join(str(_) for _ in sorted(factors)))
    except ValueError:
        return 0
