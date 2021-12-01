from .solution import Solution


def parse_entries(text: str) -> list[int]:
    return [int(i) for i in text.split()]


def count_window_increases(arr: list[int], window_size: int) -> int:
    if len(arr) <= window_size:
        return 0

    return sum(arr[i] > arr[i - window_size] for i in range(window_size, len(arr)))


def first_task(depths: list[int]) -> int:
    return count_window_increases(depths, 1)


def second_task(depths: list[int]) -> int:
    return count_window_increases(depths, 3)


class Day01(Solution):
    def first_task(self, entries_text: str) -> str:
        entries = parse_entries(entries_text)

        return str(first_task(entries))

    def second_task(self, entries_text: str) -> str:
        entries = parse_entries(entries_text)

        return str(second_task(entries))
