import operator
from typing import List, Optional, Tuple

BOUNDARY_CHAR = "|"


def _boundaries_overflow(index: int, radius: int, length: int) -> bool:
    """Checks boundaries defined by the index of the center and the radius are
    inside the sequence of given length.

    Returns True if boundaries are already outside the sequence,
    False otherwise.
    """
    return ((index + radius) >= length) or ((index - radius) < 0)


def _create_lps_table(text: str) -> List[int]:
    """Creates and returns lps table.

    To generalize even/odd length cases text is interlaced with extra char.
    Then every position in such text is considered a center of the palindrome
    and longest radius of the palindrome is found.
    """
    interlaced_text = BOUNDARY_CHAR + BOUNDARY_CHAR.join(text) + BOUNDARY_CHAR
    interlaced_text_length = len(interlaced_text)

    right_most: int = -1
    center: int = 0
    lps_table: List[int] = [None] * interlaced_text_length

    for i in range(interlaced_text_length):
        radius: Optional[int]
        if i < right_most:
            radius = min(lps_table[2 * center - i], right_most - i)
        else:
            radius = 0

        while (not _boundaries_overflow(i, radius, interlaced_text_length)) and (
            interlaced_text[i - radius] == (interlaced_text[i + radius])
        ):
            radius += 1

        lps_table[i] = radius

        current_right_most = i + radius - 1
        if current_right_most > right_most:
            center = i
            right_most = current_right_most

    return lps_table


def _get_longest_palindrome_boundaries(lps_table: List[int]) -> Tuple[int, int]:
    """Returns real text longest palindrome boundaries based from its lps table.
    """
    center_index, radius = max(enumerate(lps_table), key=operator.itemgetter(1))

    start = (center_index - (radius - 1)) // 2
    end = (center_index + radius) // 2

    return start, end


def longest_palindromic(text: str) -> str:
    """Returns longest palindromic substring (LPS) using Manacher's algorithm.

    https://en.wikipedia.org/wiki/Longest_palindromic_substring
    https://www.hackerrank.com/topics/manachers-algorithm
    """
    lps_table = _create_lps_table(text)
    start, end = _get_longest_palindrome_boundaries(lps_table)

    return text[start:end]
