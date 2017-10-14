from typing import NamedTuple


class RomanThreshold(NamedTuple):
    value: int
    writing: str


ROMAN_THRESHOLDS = [
    RomanThreshold(value=1000, writing="M"),
    RomanThreshold(value=900, writing="CM"),
    RomanThreshold(value=600, writing="DC"),
    RomanThreshold(value=500, writing="D"),
    RomanThreshold(value=400, writing="CD"),
    RomanThreshold(value=100, writing="C"),
    RomanThreshold(value=90, writing="XC"),
    RomanThreshold(value=60, writing="LX"),
    RomanThreshold(value=50, writing="L"),
    RomanThreshold(value=40, writing="XL"),
    RomanThreshold(value=10, writing="X"),
    RomanThreshold(value=9, writing="IX"),
    RomanThreshold(value=5, writing="V"),
    RomanThreshold(value=4, writing="IV"),
    RomanThreshold(value=1, writing="I"),
]


def checkio(int_number: int) -> str:
    roman_digits = []
    remainder = int_number + 0
    for threshold in ROMAN_THRESHOLDS:
        while remainder >= threshold.value:
            remainder -= threshold.value
            roman_digits.append(threshold.writing)
    return "".join(roman_digits)
