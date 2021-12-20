from __future__ import annotations
from typing import NamedTuple

INF = 10 ** 9


class Point(NamedTuple):
    row: int
    col: int


class Image:
    def __init__(self, lit_points: set[Point]) -> None:
        self.image = lit_points
        self.max_r = max(point.row for point in lit_points)
        self.min_r = min(point.row for point in lit_points)
        self.min_c = min(point.col for point in lit_points)
        self.max_c = max(point.col for point in lit_points)
        self.infinite_cell = "."

    def apply_algorithm(self, algorithm: str) -> None:
        new_image = set()
        min_r, max_r, min_c, max_c = self.min_r, self.max_r, self.min_c, self.max_c

        for row in range(min_r - 1, max_r + 2):
            for col in range(min_c - 1, max_c + 2):
                index = 0
                for i in (-1, 0, 1):
                    for j in (-1, 0, 1):
                        index *= 2
                        pos_r, pos_c = row + i, col + j

                        if (
                            pos_r < min_r
                            or pos_r > max_r
                            or pos_c < min_c
                            or pos_c > max_c
                        ):
                            index += self.infinite_cell == "#"
                        else:
                            index += (row + i, col + j) in self.image

                if algorithm[index] == "#":
                    new_image.add(Point(row, col))
                    self.min_r = min(self.min_r, row)
                    self.max_r = max(self.max_r, row)
                    self.min_c = min(self.min_c, col)
                    self.max_c = max(self.max_c, col)

        self.infinite_cell = (
            algorithm[-1] if self.infinite_cell == "#" else algorithm[0]
        )
        self.image = new_image

    @property
    def lit_points_count(self) -> int:
        return len(self.image)

    @classmethod
    def parse(cls, image: str) -> Image:
        points = set()
        for row, line in enumerate(image.split()):
            for col, cell in enumerate(line):
                if cell == "#":
                    points.add(Point(row, col))
        return cls(points)


def parse_input_image(input_image: str) -> tuple[str, Image]:
    algorithm, image = input_image.split("\n\n")

    return algorithm, Image.parse(image)


def first_task(input_image: str) -> int:
    algorithm, image = parse_input_image(input_image)

    for _ in range(2):
        image.apply_algorithm(algorithm)

    return image.lit_points_count


def second_task(input_image: str) -> int:
    algorithm, image = parse_input_image(input_image)

    for _ in range(50):
        image.apply_algorithm(algorithm)

    return image.lit_points_count
