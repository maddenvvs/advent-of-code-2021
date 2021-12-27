from __future__ import annotations

Position = tuple[int, int]


class Region:
    def __init__(
        self,
        rows: int,
        cols: int,
        east_cucumbers: set[Position],
        south_cucumbers: set[Position],
    ):
        self.rows = rows
        self.cols = cols
        self.east = east_cucumbers
        self.south = south_cucumbers

    def __str__(self) -> str:
        grid = [["."] * self.cols for _ in range(self.rows)]

        for row, col in self.east:
            grid[row][col] = ">"

        for row, col in self.south:
            grid[row][col] = "v"

        return "\n".join("".join(line) for line in grid)

    def update_positions(
        self, cucumbers: set[Position], move: Position
    ) -> tuple[set[Position], bool]:
        has_changes = False
        new_set = set()
        row_diff, col_diff = move

        for pos in cucumbers:
            new_pos = ((pos[0] + row_diff) % self.rows, (pos[1] + col_diff) % self.cols)
            if new_pos in self.east or new_pos in self.south:
                new_set.add(pos)
            else:
                new_set.add(new_pos)
                has_changes = True
        return new_set, has_changes

    def simulate_step(self) -> bool:
        self.east, east_changes = self.update_positions(self.east, move=(0, 1))
        self.south, south_changes = self.update_positions(self.south, move=(1, 0))

        return east_changes or south_changes

    @classmethod
    def parse(cls, region: str) -> Region:
        lines = region.split("\n")
        rows = len(lines)
        cols = len(lines[0])
        east = set()
        south = set()

        for row, line in enumerate(lines):
            for col, cell in enumerate(line):
                if cell == ">":
                    east.add((row, col))
                elif cell == "v":
                    south.add((row, col))

        return cls(rows, cols, east, south)


def first_task(cucumbers: str) -> int:
    region = Region.parse(cucumbers)
    steps = 1
    while region.simulate_step():
        steps += 1
    return steps


def second_task(_: str) -> str:
    return "Merry Christmas!"
