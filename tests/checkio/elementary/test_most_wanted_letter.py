from checkio.elementary.most_wanted_letter import checkio


def test_checkio():
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."

    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
