from aoc2021.day_14 import first_task, second_task

TEST_INSTRUCTIONS = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""


def test_first_task() -> None:
    assert first_task(TEST_INSTRUCTIONS) == 1588


def test_second_task() -> None:
    assert second_task(TEST_INSTRUCTIONS) == 2188189693529
