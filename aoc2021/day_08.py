from itertools import permutations

SEGMENTS_COUNT = 7


def bit(char: str) -> int:
    return ord(char) - ord("a")


def bitify(string: str) -> int:
    bits = 0
    for char in string:
        bits |= 1 << bit(char)
    return bits


DISPLAY_DIGITS = [
    bitify("abcefg"),
    bitify("cf"),
    bitify("acdeg"),
    bitify("acdfg"),
    bitify("bcdf"),
    bitify("abdfg"),
    bitify("abdefg"),
    bitify("acf"),
    bitify("abcdefg"),
    bitify("abcdfg"),
]


def parse_display(display_text: str) -> tuple[list[int], list[int]]:
    digits_str, display_str = display_text.split(" | ")
    digits = [bitify(digit) for digit in digits_str.split()]
    display = [bitify(digit) for digit in display_str.split()]
    return digits, display


def parse_displays(displays_text: str) -> list[tuple[list[int], list[int]]]:
    return [parse_display(signal) for signal in displays_text.split("\n")]


def is_valid_digit(digit: int) -> bool:
    return digit in DISPLAY_DIGITS


def decode_digit(decoding: tuple[int, ...], digit: int) -> int:
    decoded = 0
    for i, value in enumerate(decoding):
        if digit & (1 << i):
            decoded |= 1 << value
    return decoded


def is_valid_decoding(decoding: tuple[int, ...], digits: list[int]) -> bool:
    return all(is_valid_digit(decode_digit(decoding, digit)) for digit in digits)


def decode_display(decoding: tuple[int, ...], display: list[int]) -> str:
    digits = []
    for digit in display:
        digits.append(DISPLAY_DIGITS.index(decode_digit(decoding, digit)))
    return "".join(map(str, digits))


def try_decode_display(digits: list[int], display: list[int]) -> str:
    for decoding in permutations(range(SEGMENTS_COUNT)):
        if is_valid_decoding(decoding, digits):
            return decode_display(decoding, display)

    raise Exception("Couldn't find appropriate decoder")


def decode_displays(displays_text: str) -> list[str]:
    displays = parse_displays(displays_text)
    return [try_decode_display(*args) for args in displays]


def count_easy_digits(display: str) -> int:
    return sum(digit in "1478" for digit in display)


def first_task(displays_text: str) -> int:
    displays = decode_displays(displays_text)
    return sum(count_easy_digits(display) for display in displays)


def second_task(displays_text: str) -> int:
    displays = decode_displays(displays_text)
    return sum(int(display) for display in displays)
