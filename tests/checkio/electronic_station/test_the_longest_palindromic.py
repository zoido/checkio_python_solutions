from checkio.electronic_station.the_longest_palindromic import longest_palindromic


def test_longest_palindromic():
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
