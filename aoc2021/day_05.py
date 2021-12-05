from typing import NamedTuple
from collections import Counter


class Point(NamedTuple):
    x: int
    y: int

    @classmethod
    def parse(cls, point_text: str):
        return cls(*map(int, point_text.split(",")))


class Line(NamedTuple):
    start: Point
    end: Point

    @property
    def is_horizontal(self) -> bool:
        return self.start.y == self.end.y

    @property
    def is_vertical(self):
        return self.start.x == self.end.x

    @property
    def is_diagonal(self):
        return not (self.is_horizontal or self.is_vertical)

    def __iter__(self):
        if self.is_diagonal:
            d_x, d_y = ((1, 1), (1, -1))[self.start.y > self.end.y]
        else:
            d_x, d_y = ((0, 1), (1, 0))[self.is_horizontal]

        current_point = self.start
        while current_point != self.end:
            yield current_point
            current_point = Point(current_point.x + d_x, current_point.y + d_y)
        yield current_point

    @classmethod
    def parse(cls, line_text: str):
        start, end = line_text.split(" -> ")
        start_point = Point.parse(start)
        end_point = Point.parse(end)
        if start_point > end_point:
            start_point, end_point = end_point, start_point
        return cls(start_point, end_point)


def parse_lines(lines_text: str) -> list[Line]:
    return [Line.parse(l) for l in lines_text.split("\n")]


def count_intersections(lines: list[Line]) -> int:
    counter = Counter()
    for line in lines:
        for point in line:
            counter[point] += 1
    return sum(v > 1 for v in counter.values())


def first_task(lines_text: str) -> int:
    lines = parse_lines(lines_text)
    return count_intersections(line for line in lines if not line.is_diagonal)


def second_task(lines_text: str) -> int:
    lines = parse_lines(lines_text)
    return count_intersections(line for line in lines)
