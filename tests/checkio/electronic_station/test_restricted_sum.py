import hypothesis
from hypothesis import strategies

from checkio.electronic_station.restricted_sum import checkio


@hypothesis.given(numbers=strategies.lists(strategies.integers()))
def test_checkio(numbers):
    assert checkio(numbers) == sum(numbers)
