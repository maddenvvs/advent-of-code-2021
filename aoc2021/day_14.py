from collections import defaultdict


def parse_insertion(insertion: str) -> tuple[str, str]:
    pair, letter = insertion.split(" -> ")
    return pair, letter


def parse_insertions(insertions_str: str) -> dict[str, str]:
    return dict(parse_insertion(i) for i in insertions_str.split("\n"))


def parse_instructions(instructions: str) -> tuple[str, dict[str, str]]:
    template, insertions_str = instructions.split("\n\n")
    insertions = parse_insertions(insertions_str)
    return template, insertions


def simulate_one_step(
    pairs: dict[str, int], instructions: dict[str, str]
) -> dict[str, int]:
    new_pairs: dict[str, int] = defaultdict(int)

    for pair, value in pairs.items():
        letter = instructions.get(pair)
        if letter:
            new_pairs[pair[0] + letter] += value
            new_pairs[letter + pair[1]] += value

    return new_pairs


def calculate_frequencies(pairs: dict[str, int], template: str) -> dict[str, int]:
    frequencies: dict[str, int] = defaultdict(int)
    for pair, value in pairs.items():
        frequencies[pair[0]] += value
        frequencies[pair[1]] += value

    frequencies[template[0]] -= 1
    frequencies[template[-1]] -= 1

    for char in frequencies:
        frequencies[char] //= 2

    frequencies[template[0]] += 1
    frequencies[template[-1]] += 1

    return frequencies


def letters_frequency_after(
    template: str, instructions: dict[str, str], steps: int
) -> dict[str, int]:
    pairs: dict[str, int] = defaultdict(int)
    for i in range(len(template) - 1):
        pairs[template[i : i + 2]] += 1

    for _ in range(steps):
        pairs = simulate_one_step(pairs, instructions)

    return calculate_frequencies(pairs, template)


def first_task(instructions_str: str) -> int:
    template, instructions = parse_instructions(instructions_str)
    frequencies = letters_frequency_after(template, instructions, 10)
    return max(frequencies.values()) - min(frequencies.values())


def second_task(instructions_str: str) -> int:
    template, instructions = parse_instructions(instructions_str)
    frequencies = letters_frequency_after(template, instructions, 40)
    return max(frequencies.values()) - min(frequencies.values())
