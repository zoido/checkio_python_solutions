from typing import Set


def count_words(text: str, words: Set[str]) -> int:
    count = 0
    lower_text = text.lower()
    for word in words:
        if word.lower() in lower_text:
            count += 1
    return count
