def parse_entries(text: str) -> list[int]:
    return [int(i) for i in text.split()]


def count_window_increases(arr: list[int], window_size: int) -> int:
    if len(arr) <= window_size:
        return 0

    return sum(arr[i] > arr[i - window_size] for i in range(window_size, len(arr)))


def first_task(entries_text: str) -> int:
    return count_window_increases(parse_entries(entries_text), window_size=1)


def second_task(entries_text: str) -> int:
    return count_window_increases(parse_entries(entries_text), window_size=3)
