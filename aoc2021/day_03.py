from typing import Callable


def parse_diagnostic_report(report_text: str) -> list[str]:
    return report_text.split("\n")


def find_power_consumption(report: list[str]) -> int:
    n = len(report)
    bits = len(report[0])
    freq = [0] * bits

    for line in report:
        for i, ch in enumerate(line):
            freq[i] += ch == "1"

    gamma_rate = 0
    for v in freq:
        gamma_rate *= 2
        gamma_rate += 2 * v > n

    epsilon_rate = ~gamma_rate & ((1 << bits) - 1)

    return gamma_rate * epsilon_rate


def find_element(report: list[str], decider: Callable[[int, int, int], bool]) -> str:
    bits = len(report[0])
    l, r = 0, len(report)

    for bit_pos in range(bits):
        zeroes = 0
        for i in range(l, r):
            if report[i][bit_pos] == "0":
                report[l + zeroes], report[i] = report[i], report[l + zeroes]
                zeroes += 1

        if decider(l, r, zeroes):
            r = l + zeroes
        else:
            l = l + zeroes

    return report[l]


def oxygen_generator_rating(report: list[str]) -> int:
    return int(find_element(report, lambda l, r, zeroes: zeroes * 2 > (r - l)), base=2)


def co2_scrubber_rating(report: list[str]) -> int:
    return int(find_element(report, lambda l, r, zeroes: zeroes * 2 <= (r - l)), base=2)


def calculate_life_support_rating(report: list[str]) -> int:
    return oxygen_generator_rating(report) * co2_scrubber_rating(report)


def first_task(binary_text: str) -> int:
    return find_power_consumption(parse_diagnostic_report(binary_text))


def second_task(binary_text: str) -> int:
    return calculate_life_support_rating(parse_diagnostic_report(binary_text))
