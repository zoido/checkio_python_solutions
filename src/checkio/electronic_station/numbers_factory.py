from typing import Generator, Iterable


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
        if n < 10 or not divided:
            yield n
            break


def compress_factors(factors: Iterable[int]) -> Iterable[int]:
    result = []
    accumulator = 1
    for f in list(factors):
        if f > 9:
            return [0]
        accumulator *= f
        if accumulator > 9:
            result.append(accumulator // f)
            accumulator = f
    result.append(accumulator)
    return result


def checkio(number: int) -> int:
    factors = sorted(find_factors(number))
    compressed_factors = compress_factors(factors)
    return int("".join(str(_) for _ in sorted(compressed_factors)))
