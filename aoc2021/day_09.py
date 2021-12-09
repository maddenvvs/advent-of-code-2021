from typing import Generator

HeightMap = list[list[int]]

DIRECTIONS = ((0, 1), (0, -1), (1, 0), (-1, 0))


def risk_level(value: int) -> int:
    return value + 1


def low_points(heightmap: HeightMap) -> Generator[tuple[int, int], None, None]:
    for row, line in enumerate(heightmap):
        for column, cell in enumerate(line):
            if cell == 9:
                continue

            for row_diff, col_diff in DIRECTIONS:
                new_row, new_col = row + row_diff, column + col_diff

                if heightmap[new_row][new_col] <= cell:
                    break
            else:
                yield row, column


def basins(heightmap: HeightMap) -> Generator[int, None, None]:
    def basin_size(row: int, col: int) -> int:
        heightmap[row][col] = 9
        stack = [(row, col)]
        size = 0

        while stack:
            curr_row, curr_col = stack.pop()

            size += 1

            for row_diff, col_diff in DIRECTIONS:
                new_row, new_col = curr_row + row_diff, curr_col + col_diff

                if heightmap[new_row][new_col] == 9:
                    continue

                heightmap[new_row][new_col] = 9
                stack.append((new_row, new_col))

        return size

    for row, line in enumerate(heightmap):
        for column, cell in enumerate(line):
            if cell != 9:
                yield basin_size(row, column)


def parse_heightmap(heightmap_str: str) -> HeightMap:
    heightmap = [[9] + list(map(int, line)) + [9] for line in heightmap_str.split()]
    cols = len(heightmap[0])
    return [[9] * cols] + heightmap + [[9] * cols]


def first_task(heightmap_str: str) -> int:
    heightmap = parse_heightmap(heightmap_str)

    total_risk_level = 0
    for row, col in low_points(heightmap):
        total_risk_level += risk_level(heightmap[row][col])

    return total_risk_level


def second_task(heightmap_str: str) -> int:
    heightmap = parse_heightmap(heightmap_str)
    first, second, third = 0, 0, 0

    for basin_size in basins(heightmap):

        if basin_size >= first:
            first, second, third = basin_size, first, second
        elif basin_size >= second:
            second, third = basin_size, second
        elif basin_size > third:
            third = basin_size

    return first * second * third
