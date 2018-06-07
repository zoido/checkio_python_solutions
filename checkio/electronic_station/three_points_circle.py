import decimal
import itertools
from typing import List, NamedTuple, Tuple


class Point(NamedTuple):
    x: decimal.Decimal
    y: decimal.Decimal


def parse_points(points_str: str) -> List[Point]:
    single_point_strings = points_str[1:-1].split("),(")
    coordinates = (point_string.split(",")
                   for point_string in single_point_strings)
    return [
        Point(x=decimal.Decimal(x), y=decimal.Decimal(y))
        for x, y in coordinates
    ]


def get_slope(point_a: Point, point_b: Point) -> decimal.Decimal:
    """Returns the slope of the line connecting tho points passed as parameters.
    """
    return (point_b.y - point_a.y) / (point_b.x - point_a.x)


def get_distance(point_a: Point, point_b: Point) -> decimal.Decimal:
    """Returns the distance between two points."""
    return (((point_b.x - point_a.x)**2) +
            (((point_b.y - point_a.y)**2))).sqrt()


def find_the_order(point_a: Point, point_b: Point,
                   point_c: Point) -> Tuple[Point, Point, Point]:
    """Returns points in the order when slopes of lines are defined."""
    for pa, pb, pc in itertools.permutations([point_a, point_b, point_c]):
        try:
            get_slope(pa, pb)
            get_slope(pb, pc)
        except decimal.DivisionByZero:
            continue
        else:
            return pa, pb, pc
    raise ValueError("Circle cannot be constructed.")  # pragma: no cover


def format_coordinate(number: decimal.Decimal) -> str:
    """Returns decimal in the format required by task.

    2.0000 -> 2
    2.104 -> 2.1
    """
    return "{:.2f}".format(number).rstrip("0").rstrip(".")


def checkio(points_str: str) -> str:
    point_a, point_b, point_c = find_the_order(*parse_points(points_str))

    slope_ab = get_slope(point_a, point_b)
    slope_bc = get_slope(point_b, point_c)

    center_x = ((slope_ab * slope_bc * (point_a.y - point_c.y)) +
                (slope_bc * (point_a.x + point_b.x)) -
                (slope_ab * (point_b.x + point_c.x))) / (2 *
                                                         (slope_bc - slope_ab))
    center_y: decimal.Decimal
    try:
        center_y = ((-1 / slope_bc) * (center_x - (
            (point_b.x + point_c.x) / 2))) + ((point_b.y + point_c.y) / 2)
    except decimal.DivisionByZero:
        center_y = ((-1 / slope_ab) * (center_x - (
            (point_a.x + point_b.x) / 2))) + ((point_a.y + point_b.y) / 2)

    center = Point(x=center_x, y=center_y)
    radius = get_distance(point_a, center)

    center_x_str = format_coordinate(center_x)
    center_y_str = format_coordinate(center_y)
    radius_str = format_coordinate(radius)

    return f"(x-{center_x_str})^2+(y-{center_y_str})^2={radius_str}^2"
