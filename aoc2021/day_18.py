from __future__ import annotations
from typing import Generator, Optional, cast


class SnailfishNumber:
    def __init__(
        self,
        *,
        value: int = -1,
        left: Optional[SnailfishNumber] = None,
        right: Optional[SnailfishNumber] = None,
        parent: Optional[SnailfishNumber] = None,
    ) -> None:
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    @property
    def is_regular(self) -> bool:
        return self.value != -1

    @property
    def is_pair(self) -> bool:
        return not self.is_regular

    def magnitude(self) -> int:
        if self.is_regular:
            return self.value

        left = cast(SnailfishNumber, self.left)
        right = cast(SnailfishNumber, self.right)
        return 3 * left.magnitude() + 2 * right.magnitude()

    def regular_numbers(
        self, depth: int = 0
    ) -> Generator[tuple[SnailfishNumber, int], None, None]:
        if self.is_regular:
            yield self, depth
        else:
            left = cast(SnailfishNumber, self.left)
            right = cast(SnailfishNumber, self.right)

            yield from left.regular_numbers(depth + 1)
            yield from right.regular_numbers(depth + 1)

    def simplify(self) -> None:
        self.explode()
        self.split()

    def explode(self) -> None:
        prev, curr, nxt = None, None, None

        for regular_number, depth in self.regular_numbers():
            if curr is not None:
                if regular_number is not curr.right:
                    nxt = regular_number
                    break
            elif depth > 4:
                curr = regular_number.parent
            else:
                prev = regular_number

        if curr is None:
            return

        left = cast(SnailfishNumber, curr.left)
        right = cast(SnailfishNumber, curr.right)

        if prev:
            prev.value += left.value
        if nxt:
            nxt.value += right.value

        curr.value = 0
        curr.left = curr.right = None

        self.simplify()

    def split(self) -> None:
        for regular_number, _ in self.regular_numbers():
            if regular_number.value > 9:
                value = regular_number.value
                left = value // 2
                right = value - left

                new_number = SnailfishNumber.pair(
                    SnailfishNumber.regular_number(left),
                    SnailfishNumber.regular_number(right),
                )
                parent = cast(SnailfishNumber, regular_number.parent)
                if parent.left == regular_number:
                    parent.left = new_number
                else:
                    parent.right = new_number
                new_number.parent = parent

                self.simplify()

                break

    def clone(self) -> SnailfishNumber:
        if self.is_regular:
            return SnailfishNumber.regular_number(self.value)

        left = cast(SnailfishNumber, self.left)
        right = cast(SnailfishNumber, self.right)

        return SnailfishNumber.pair(left.clone(), right.clone())

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        if self.is_regular:
            return str(self.value)

        return f"[{str(self.left)},{str(self.right)}]"

    def __add__(self, other: SnailfishNumber) -> SnailfishNumber:
        pair = SnailfishNumber.pair(self, other)
        pair.simplify()
        return pair

    @classmethod
    def regular_number(cls, value: int) -> SnailfishNumber:
        return cls(value=value)

    @classmethod
    def pair(cls, left: SnailfishNumber, right: SnailfishNumber) -> SnailfishNumber:
        parent = cls(left=left, right=right)
        left.parent = right.parent = parent
        return parent

    @classmethod
    def parse(cls, snailfish: str) -> SnailfishNumber:
        stack = []
        for char in snailfish:
            if char in "[,":
                continue

            if char.isdigit():
                stack.append(cls.regular_number(int(char)))
            else:
                second = stack.pop()
                first = stack.pop()
                stack.append(cls.pair(first, second))

        return stack[0]


def add_all(numbers: list[SnailfishNumber]) -> SnailfishNumber:
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = result + numbers[i]
    return result


def find_largest_magnitude(numbers: list[SnailfishNumber]) -> int:
    largest_magnitude = 0

    for i, first in enumerate(numbers):
        for j, second in enumerate(numbers):
            if i == j:
                continue
            largest_magnitude = max(
                largest_magnitude, (first.clone() + second.clone()).magnitude()
            )

    return largest_magnitude


def parse_homework(homework: str) -> list[SnailfishNumber]:
    return [SnailfishNumber.parse(s) for s in homework.split("\n")]


def first_task(homework: str) -> int:
    numbers = parse_homework(homework)
    return add_all(numbers).magnitude()


def second_task(homework: str) -> int:
    numbers = parse_homework(homework)
    return find_largest_magnitude(numbers)
