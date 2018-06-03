import pytest

from checkio.electronic_station.three_points_circle import checkio


def test_checkio():
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"


def test_fails():
    checkio("(9,8),(9,4),(3,6)")
    checkio("(7,3),(9,6),(3,6)")


def test_throws_value_error_when_points_are_in_line():
    with pytest.raises(ValueError) as exception_info:
        checkio("(9,8),(9,4),(9,6)")

    assert "Circle cannot be constructed" in str(exception_info.value)
