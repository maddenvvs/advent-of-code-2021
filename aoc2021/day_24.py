# pylint: disable=line-too-long
# Inspired by https://www.reddit.com/r/adventofcode/comments/rnejv5/comment/hps4c3n/?utm_source=share&utm_medium=web2x&context=3

from typing import Iterator
from functools import reduce

class ALU:
    def __init__(self, program: list[list[str]]):
        self.program = program
        self.reset()

    def reset(self) -> None:
        self.vars = {v: 0 for v in "wxyz"}

    def get_operand_values(self, left: str, right: str) -> tuple[int, int]:
        left_value = self.vars[left]
        right_value = self.vars[right] if right in "wxyz" else int(right)
        return left_value, right_value

    def run(self, input_line: str = "") -> None:
        inp_idx = 0

        for line in self.program:
            match line.split():
                case ["inp", variable]:
                    self.vars[variable] = int(input_line[inp_idx])
                    inp_idx += 1
                case ["add", op_a, op_b]:
                    left, right = self.get_operand_values(op_a, op_b)
                    self.vars[op_a] = left + right
                case ["mul", op_a, op_b]:
                    left, right = self.get_operand_values(op_a, op_b)
                    self.vars[op_a] = left * right
                case ["div", op_a, op_b]:
                    left, right = self.get_operand_values(op_a, op_b)
                    self.vars[op_a] = left // right
                case ["mod", op_a, op_b]:
                    left, right = self.get_operand_values(op_a, op_b)
                    self.vars[op_a] = left % right
                case ["eql", op_a, op_b]:
                    left, right = self.get_operand_values(op_a, op_b)
                    self.vars[op_a] = int(left == right)

def skip(iterator: Iterator, times: int) -> None:
    for _ in range(times):
        next(iterator)

def get_constraints(program: Iterator) -> list[tuple[int, int, int]]:
    constraints = []
    stack = []

    for i in range(14):
        skip(program, 4)
        instruction = next(program).rstrip()

        if instruction == 'div z 1':
            skip(program, 10)
            instruction = next(program)

            operand_a = int(instruction.split()[-1])
            stack.append((i, operand_a))
            skip(program, 2)
        else:
            instruction = next(program)

            operand_b = int(instruction.split()[-1])
            j, operand_a = stack.pop()
            constraints.append((i, j, operand_a + operand_b))
            skip(program, 12)

    return constraints


def find_numbers_pair(program: list[list[str]]) -> tuple[int, int]:
    constraints = get_constraints(iter(program))
    nmax = [0] * 14
    nmin = [0] * 14

    for i, j, diff in constraints:
        if diff > 0:
            nmax[i], nmax[j] = 9, 9 - diff
            nmin[i], nmin[j] = 1 + diff, 1
        else:
            nmax[i], nmax[j] = 9 + diff, 9
            nmin[i], nmin[j] = 1, 1 - diff

    nmax = reduce(lambda acc, d: acc * 10 + d, nmax)
    nmin = reduce(lambda acc, d: acc * 10 + d, nmin)
    return nmax, nmin


def parse_program(program: str) -> list[str]:
    return program.split("\n")


def first_task(program_str: str) -> int:
    program = parse_program(program_str)
    max_number, _ = find_numbers_pair(program)
    return max_number

def second_task(program_str: str) -> int:
    program = parse_program(program_str)
    _, min_number = find_numbers_pair(program)
    return min_number
