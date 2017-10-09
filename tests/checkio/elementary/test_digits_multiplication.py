from checkio.elementary.digits_multiplication import checkio


def test_checkio():
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
