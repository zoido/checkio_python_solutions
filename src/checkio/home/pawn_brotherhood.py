import itertools
from typing import NamedTuple, Set

LETTERS_OFFSET = ord("a") - 1


class Position(NamedTuple):
    x: int
    y: int


def _to_positions(str_coordinates: Set[str]):
    coordinates: Set[tuple] = set()
    for c in str_coordinates:
        x, y = tuple(c)
        position = Position(x=ord(x) - LETTERS_OFFSET, y=int(y))
        coordinates.add(position)
    return coordinates


def _reachable_coordinates(position: Position) -> Set[Position]:
    return {
        Position(x=position.x - 1, y=position.y + 1),
        Position(x=position.x + 1, y=position.y + 1),
    }


def safe_pawns(str_coordinates: Set[str]) -> int:
    coordinates = _to_positions(str_coordinates)
    safe_coordinates = set(
        itertools.chain.from_iterable(
            _reachable_coordinates(p) for p in coordinates))

    return len(coordinates & safe_coordinates)
