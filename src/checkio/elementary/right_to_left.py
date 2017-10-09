from typing import Sequence


def left_join(words: Sequence[str]) -> str:
    return ",".join(words).replace("right", "left")
