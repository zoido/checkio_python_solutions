from checkio.home.long_repeat import long_repeat


def test_long_repeat():
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"


def test_fails_1():
    assert long_repeat('') == 0, "Empty String"


def test_fails_2():
    assert long_repeat('aa') == 2
