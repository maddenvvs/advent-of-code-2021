from __future__ import annotations
from typing import NamedTuple

INFINITY = 10 ** 9


class Instruction(NamedTuple):
    axis: str
    value: int

    @classmethod
    def parse(cls, instruction_str: str) -> Instruction:
        left, right = instruction_str.split("=")
        value = int(right)
        axis = left[-1]
        return cls(axis, value)


class Point(NamedTuple):
    x: int
    y: int

    @classmethod
    def parse(cls, point: str) -> Point:
        return cls(*map(int, point.split(",")))


class Paper:
    def __init__(self, dots: set[Point]) -> None:
        self.dots = dots

    @property
    def visible_points(self) -> int:
        return len(self.dots)

    # pylint: disable-next=invalid-name
    def fold_x(self, x: int) -> None:
        new_dots = set()

        for dot in self.dots:
            if dot.x <= x:
                new_dots.add(dot)
            else:
                new_dots.add(Point(2 * x - dot.x, dot.y))

        self.dots = new_dots

    # pylint: disable-next=invalid-name
    def fold_y(self, y: int) -> None:
        new_dots = set()

        for dot in self.dots:
            if dot.y <= y:
                new_dots.add(dot)
            else:
                new_dots.add(Point(dot.x, 2 * y - dot.y))

        self.dots = new_dots

    def apply_instruction(self, instruction: Instruction) -> None:
        axis, value = instruction
        if axis == "x":
            self.fold_x(value)
        else:
            self.fold_y(value)

    def __str__(self) -> str:
        min_x, max_x = INFINITY, 0
        min_y, max_y = INFINITY, 0

        # pylint: disable-next=invalid-name
        for x, y in self.dots:
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

        width, height = max_x - min_x + 1, max_y - min_y + 1
        grid = [["."] * width for _ in range(height)]

        # pylint: disable-next=invalid-name
        for x, y in self.dots:
            grid[y - min_y][x - min_x] = "#"

        return "\n".join("".join(row) for row in grid)

    @classmethod
    def parse(cls, points_str: str) -> Paper:
        points_list = points_str.split("\n")
        points = {Point.parse(p) for p in points_list}
        return cls(points)


def parse_origami(origami: str) -> tuple[Paper, list[Instruction]]:
    paper_str, instructions_str = origami.split("\n\n")
    paper = Paper.parse(paper_str)
    instructions = [Instruction.parse(i) for i in instructions_str.split("\n")]
    return paper, instructions


def first_task(origami: str) -> int:
    paper, instructions = parse_origami(origami)
    paper.apply_instruction(instructions[0])
    return paper.visible_points


def second_task(origami: str) -> str:
    paper, instructions = parse_origami(origami)
    for instruction in instructions:
        paper.apply_instruction(instruction)
    return "\n" + str(paper)
