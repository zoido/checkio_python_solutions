from checkio.home.xs_and_os_referee import checkio


def test_checkio():
    assert checkio(["X.O", "XX.", "XOO"]) == "X", "Xs wins"
    assert checkio(["OO.", "XOX", "XOX"]) == "O", "Os wins"
    assert checkio(["OOX", "XXO", "OXX"]) == "D", "Draw"
    assert checkio(["O.X", "XX.", "XOO"]) == "X", "Xs wins again"


def test_fail_1():
    checkio(["...", "XXX", "OO."])
    # does not throw exception


def test_fail_2():
    assert checkio(["OOO", "XX.", ".XX"]) == "O"
