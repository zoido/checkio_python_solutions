from checkio.home.monkey_typing import count_words


def test_checkio():
    assert (
        count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3
    ), "Example"
    assert (
        count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2
    ), "BANANAS!"
    assert (
        count_words(
            "Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
            {"sum", "hamlet", "infinity", "anything"},
        )
        == 1
    ), "Weird text"
