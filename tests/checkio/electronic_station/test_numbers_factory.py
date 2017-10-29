import functools
import operator

import hypothesis
from hypothesis import strategies

from checkio.electronic_station.numbers_factory import checkio, find_factors


@hypothesis.given(number=strategies.integers(min_value=10))
def test_find_factors(number):
    # when
    result = find_factors(number)

    # then
    assert functools.reduce(operator.mul, result) == number


def test_checkio():
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"


def test_fail_1():
    assert checkio(560) == 2578


def test_fail_2():
    assert checkio(3275) == 0


def test_fail_3():
    assert checkio(1536) == 3888


def test_fail_4():
    assert checkio(12) == 26
