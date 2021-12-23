from __future__ import annotations
from typing import NamedTuple
from itertools import product

INFINITY = 10 ** 18


class Cell(NamedTuple):
    row: int
    col: int

    def add(self, other: Cell) -> Cell:
        return Cell(self.row + other.row, self.col + other.col)

    def manhattan(self, other: Cell) -> int:
        return abs(self.row - other.row) + abs(self.col - other.col)


DIRECTIONS = (Cell(0, 1), Cell(1, 0), Cell(0, -1), Cell(-1, 0))

POSSIBLE_HALLWAY_CELLS = set(
    [
        Cell(1, 1),
        Cell(1, 2),
        Cell(1, 4),
        Cell(1, 6),
        Cell(1, 8),
        Cell(1, 10),
        Cell(1, 11),
    ]
)

MOVE_COST = {"A": 1, "B": 10, "C": 100, "D": 1000}


def count_energy_cost(start: Cell, end: Cell, amph_type: str) -> int:
    return start.manhattan(end) * MOVE_COST[amph_type]


class Burrow:
    def __init__(
        self,
        init_positions: dict[str, Cell],
        coridors: set[Cell],
        destination_rooms: dict[str, list[Cell]],
    ):
        self.amphipods = init_positions
        self.coridors = coridors
        self.cache: dict[tuple[Cell, ...], int] = {}
        self.destination_rooms = destination_rooms
        self.destination_rooms_sets = {k: set(v) for k, v in destination_rooms.items()}

    def generate_cache_key(self) -> tuple[Cell, ...]:
        return tuple(
            self.amphipods[f"{key}{num}"]
            for key, num in product("ABCD", range(1, len(self.amphipods) // 4 + 1))
        )

    def all_amphipods_are_in_positions(self) -> bool:
        return all(
            pos in self.destination_rooms_sets[a[0]]
            for a, pos in self.amphipods.items()
        )

    def find_amph_at_position(self, position: Cell) -> str:
        arr = [a for a, pos in self.amphipods.items() if pos == position]
        return arr[0] if arr else ""
        # return next(a for a, pos in self.amphipods.items() if pos == position)

    def is_reachable(self, start: Cell, end: Cell) -> bool:
        stack = [start]
        visited = set(self.amphipods.values())
        visited.add(start)

        while stack:
            curr = stack.pop()
            if curr == end:
                return True

            for direction in DIRECTIONS:
                new_pos = curr.add(direction)
                if new_pos not in self.coridors:
                    continue
                if new_pos in visited:
                    continue
                visited.add(new_pos)
                stack.append(new_pos)

        return False

    def is_room_with_friends(self, amph: str) -> bool:
        amph_type = amph[0]
        position = self.amphipods[amph]
        rooms = self.destination_rooms[amph_type]
        if position not in rooms:
            return False

        room_idx = rooms.index(position)
        return all(
            self.find_amph_at_position(rooms[idx])[0] == amph_type
            for idx in range(room_idx)
        )

    def try_find_room_cell(self, amph: str) -> list[Cell]:
        amph_type = amph[0]
        position = self.amphipods[amph]
        rooms = self.destination_rooms[amph_type]

        for room in rooms:
            room_amph = self.find_amph_at_position(room)
            if room_amph:
                if room_amph[0] == amph_type:
                    continue

                return []

            if self.is_reachable(position, room):
                return [room]

            return []

        return []

    def try_find_hallway_cell(self, amph: str) -> list[Cell]:
        position = self.amphipods[amph]
        return [
            cell for cell in POSSIBLE_HALLWAY_CELLS if self.is_reachable(position, cell)
        ]

    def find_possible_moves_for(self, amph: str) -> list[Cell]:
        position = self.amphipods[amph]

        if position in POSSIBLE_HALLWAY_CELLS:
            return self.try_find_room_cell(amph)

        if self.is_room_with_friends(amph):
            return []

        return self.try_find_hallway_cell(amph)

    def find_possible_moves(self) -> list[tuple[str, Cell]]:
        moves: list[tuple[str, Cell]] = []
        for amph in self.amphipods:
            moves += ((amph, move) for move in self.find_possible_moves_for(amph))
        return moves

    def find_min_energy(self) -> int:
        if self.all_amphipods_are_in_positions():
            return 0

        cache_key = self.generate_cache_key()
        cache_value = self.cache.get(cache_key, -1)
        if cache_value != -1:
            return cache_value

        min_energy = INFINITY
        for amph, new_pos in self.find_possible_moves():
            prev_pos = self.amphipods[amph]
            energy_cost = count_energy_cost(prev_pos, new_pos, amph[0])
            self.amphipods[amph] = new_pos
            min_energy = min(min_energy, self.find_min_energy() + energy_cost)
            self.amphipods[amph] = prev_pos

        self.cache[cache_key] = min_energy

        return min_energy

    @classmethod
    def parse(cls, burrow: str) -> Burrow:
        positions = {}
        coridors = set()
        counter = {char: 1 for char in "ABCD"}
        lines = burrow.split("\n")

        for row, line in enumerate(lines):
            for col, cell in enumerate(line):
                if cell in "ABCD":
                    positions[f"{cell}{counter[cell]}"] = Cell(row, col)
                    counter[cell] += 1

                if cell in ".ABCD":
                    coridors.add(Cell(row, col))

        destination_rooms = {
            char: [Cell(row, col) for row in range(len(lines) - 2, 1, -1)]
            for char, col in zip("ABCD", (3, 5, 7, 9))
        }

        return cls(positions, coridors, destination_rooms)


def expand_burrow(burrow: str) -> str:
    lines = burrow.split("\n")
    return "\n".join(lines[:-2] + ["  #D#C#B#A#", "  #D#B#A#C#"] + lines[-2:])


def first_task(burrow_str: str) -> int:
    burrow = Burrow.parse(burrow_str)
    return burrow.find_min_energy()


def second_task(burrow_str: str) -> int:
    burrow = Burrow.parse(expand_burrow(burrow_str))
    return burrow.find_min_energy()
