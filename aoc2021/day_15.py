from typing import Iterable
import heapq


def parse_cavern(cavern: str) -> list[list[int]]:
    return [list(map(int, line)) for line in cavern.split()]


def find_min_path_score_scaled(
    cavern: list[list[int]], scale_width: int = 1, scale_height: int = 1
) -> int:
    # pylint: disable=too-many-locals

    def count_risk_level(row: int, col: int) -> int:
        risk_row_diff, risk_row = divmod(row, rows_count)
        risk_col_diff, risk_col = divmod(col, cols_count)
        risk_level = cavern[risk_row][risk_col] + risk_row_diff + risk_col_diff
        if risk_level > 9:
            risk_level -= 9
        return risk_level

    def neighbours(row: int, col: int) -> Iterable[tuple[int, int]]:
        for diff_row, diff_col in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            new_row, new_col = row + diff_row, col + diff_col
            if new_row < 0 or new_row >= height or new_col < 0 or new_col >= width:
                continue
            yield new_row, new_col

    rows_count = len(cavern)
    cols_count = len(cavern[0])
    width = scale_width * cols_count
    height = scale_height * rows_count
    risk = [[10 ** 9] * width for _ in range(height)]
    risk[0][0] = 0
    queue = [(0, 0, 0)]

    while queue:
        curr_risk, curr_row, curr_col = heapq.heappop(queue)

        if risk[curr_row][curr_col] != curr_risk:
            continue

        for new_row, new_col in neighbours(curr_row, curr_col):
            new_risk = curr_risk + count_risk_level(new_row, new_col)
            if risk[new_row][new_col] > new_risk:
                risk[new_row][new_col] = new_risk
                heapq.heappush(queue, (new_risk, new_row, new_col))

    return risk[-1][-1]


def first_task(cavern_str: str) -> int:
    cavern = parse_cavern(cavern_str)
    return find_min_path_score_scaled(cavern)


def second_task(cavern_str: str) -> int:
    cavern = parse_cavern(cavern_str)
    return find_min_path_score_scaled(cavern, 5, 5)
