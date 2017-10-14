from checkio.electronic_station.brackets import checkio


def test_checkio():
    assert checkio("((5+3)*2+1)") is True, "Simple"
    assert checkio("{[(3+1)+2]+}") is True, "Different types"
    assert checkio("(3+{1-1)}") is False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") is True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") is False, "One is redundant"
    assert checkio("2+3") is True, "No brackets, no problem"


def test_fail_1():
    assert checkio("(((1+(1+1))))]") is False, "Extra pop"
