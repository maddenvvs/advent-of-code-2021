from __future__ import annotations

DIRECTIONS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))


class Grid:
    def __init__(self, grid: list[list[int]]) -> None:
        self.grid = grid
        self.size = len(self.grid)

    def simulate_one_step(self) -> int:
        stack = []
        size = self.size

        for row, line in enumerate(self.grid):
            for col, energy in enumerate(line):
                if energy == 9:
                    stack.append((row, col))
                self.grid[row][col] = (energy + 1) % 10

        flashes = 0
        while stack:
            curr_row, curr_col = stack.pop()
            flashes += 1

            for diff_row, diff_col in DIRECTIONS:
                new_row, new_col = curr_row + diff_row, curr_col + diff_col
                if new_row < 0 or new_row >= size or new_col < 0 or new_col >= size:
                    continue

                energy = self.grid[new_row][new_col]
                if energy == 0:
                    continue

                if energy == 9:
                    stack.append((new_row, new_col))
                self.grid[new_row][new_col] = (energy + 1) % 10

        return flashes

    def simulate_multiple_steps(self, steps: int) -> int:
        return sum(self.simulate_one_step() for _ in range(steps))

    def find_synchronization_step(self) -> int:
        expected_flashes = self.size ** 2
        steps = 1

        while self.simulate_one_step() != expected_flashes:
            steps += 1

        return steps

    def __str__(self) -> str:
        return "\n".join("".join(map(str, row)) for row in self.grid)

    @classmethod
    def parse(cls, grid_str: str) -> Grid:
        grid = [[int(i) for i in row] for row in grid_str.split("\n")]
        return cls(grid)


def first_task(octopuses: str) -> int:
    grid = Grid.parse(octopuses)
    return grid.simulate_multiple_steps(100)


def second_task(octopuses: str) -> int:
    grid = Grid.parse(octopuses)
    return grid.find_synchronization_step()
