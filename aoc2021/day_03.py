from typing import Callable


def parse_diagnostic_report(report_text: str) -> list[str]:
    return report_text.split("\n")


def find_gamma_rate(report: list[str]) -> int:
    lines_count, bits_count = len(report), len(report[0])
    gamma_rate = 0

    for bit_pos in range(bits_count):
        ones = 0
        for line in report:
            ones += line[bit_pos] == "1"

        gamma_rate *= 2
        gamma_rate += 2 * ones > lines_count

    return gamma_rate


def find_power_consumption(report: list[str]) -> int:
    bits = len(report[0])

    gamma_rate = find_gamma_rate(report)
    epsilon_rate = ~gamma_rate & ((1 << bits) - 1)

    return gamma_rate * epsilon_rate


def find_element(report: list[str], decider: Callable[[int, int], bool]) -> str:
    bits = len(report[0])
    left, right = 0, len(report)

    for bit_pos in range(bits):
        zeroes = 0
        for i in range(left, right):
            if report[i][bit_pos] == "0":
                report[left + zeroes], report[i] = report[i], report[left + zeroes]
                zeroes += 1

        if decider(right - left, zeroes):
            right = left + zeroes
        else:
            left = left + zeroes

    return report[left]


def oxygen_generator_rating(report: list[str]) -> int:
    return int(find_element(report, lambda total, zeroes: zeroes * 2 > total), base=2)


def co2_scrubber_rating(report: list[str]) -> int:
    return int(find_element(report, lambda total, zeroes: zeroes * 2 <= total), base=2)


def calculate_life_support_rating(report: list[str]) -> int:
    return oxygen_generator_rating(report) * co2_scrubber_rating(report)


def first_task(binary_text: str) -> int:
    return find_power_consumption(parse_diagnostic_report(binary_text))


def second_task(binary_text: str) -> int:
    return calculate_life_support_rating(parse_diagnostic_report(binary_text))
