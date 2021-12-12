import pytest
from aoc2021.day_12 import first_task, second_task


@pytest.mark.parametrize(
    "caves,expected_paths",
    [
        (
            """start-A
start-b
A-c
A-b
b-d
A-end
b-end""",
            10,
        ),
        (
            """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc""",
            19,
        ),
        (
            """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW""",
            226,
        ),
    ],
)
def test_first_task(caves: str, expected_paths: int) -> None:
    assert first_task(caves) == expected_paths


@pytest.mark.parametrize(
    "caves,expected_paths",
    [
        (
            """start-A
start-b
A-c
A-b
b-d
A-end
b-end""",
            36,
        ),
        (
            """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc""",
            103,
        ),
        (
            """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW""",
            3509,
        ),
    ],
)
def test_second_task(caves: str, expected_paths: int) -> None:
    assert second_task(caves) == expected_paths
