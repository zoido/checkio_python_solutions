import itertools
from typing import List, Sequence


def _get_winner(triple: Sequence) -> str:
    if "".join(triple) == "XXX":
        return "X"

    if "".join(triple) == "OOO":
        return "O"

    return "D"


def _get_diagonals(game_result: Sequence) -> List[List]:
    return [
        [game_result[0][0], game_result[1][1], game_result[2][2]],
        [game_result[0][2], game_result[1][1], game_result[2][0]],
    ]


def checkio(game_result: Sequence[str]) -> str:
    transposed_results = list(map(list, zip(*game_result)))

    row_winners = [_get_winner(row) for row in game_result]
    column_winners = [_get_winner(column) for column in transposed_results]
    diagonal_winners = [
        _get_winner(diagonal) for diagonal in _get_diagonals(game_result)
    ]

    verdict_set = set(itertools.chain(row_winners, column_winners, diagonal_winners))

    return ((list(verdict_set - {"D"})) or "D")[0]
