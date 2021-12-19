from __future__ import annotations
from typing import NamedTuple, Optional, Generator, Union
from collections import deque


class Vector(NamedTuple):
    x: int
    y: int
    z: int

    def __add__(self, other: object) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

        raise Exception("Unsupported operand", other)

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

        raise Exception("Unsupported operand", other)

    def dot(self, other: Union[list, Vector]) -> int:
        return sum(a * b for a, b in zip(self, other))

    def manhattan(self) -> int:
        return abs(self.x) + abs(self.y) + abs(self.z)

    @classmethod
    def parse(cls, vector: str) -> Vector:
        return cls(*map(int, vector.split(",")))


class Orientation:
    def __init__(self, matrix: Optional[list[list[int]]] = None) -> None:
        self.matrix = matrix or [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    def __repr__(self) -> str:
        return str(self.matrix)

    def multiply_orientation(self, other: Orientation) -> Orientation:
        new_matrix = [[0] * 3 for _ in range(3)]

        for i in range(3):
            for j in range(3):
                for k in range(3):
                    new_matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]

        return Orientation(new_matrix)

    def multiply_vector(self, other: Vector) -> Vector:
        return Vector(*(other.dot(row) for row in self.matrix))

    def rotate_x(self) -> Orientation:
        return Orientation([[1, 0, 0], [0, 0, 1], [0, -1, 0]]).multiply_orientation(
            self
        )

    def rotate_y(self) -> Orientation:
        return Orientation([[0, 0, 1], [0, 1, 0], [-1, 0, 0]]).multiply_orientation(
            self
        )

    def rotate_z(self) -> Orientation:
        return Orientation([[0, 1, 0], [-1, 0, 0], [0, 0, 1]]).multiply_orientation(
            self
        )


class Scanner(NamedTuple):
    identifier: int
    beacons: list[Vector]

    @classmethod
    def parse(cls, scanner_info: str) -> Scanner:
        lines = scanner_info.split("\n")
        first_line_parts = lines[0].split()
        _id = int(first_line_parts[2])
        points = [Vector.parse(lines[i]) for i in range(1, len(lines))]
        return cls(_id, points)


def possible_orientations() -> Generator[Orientation, None, None]:
    orientation = Orientation()

    for _ in range(4):
        for _ in range(4):
            yield orientation
            orientation = orientation.rotate_x()
        orientation = orientation.rotate_y()

    orientation = orientation.rotate_z()
    for _ in range(2):
        for _ in range(4):
            yield orientation
            orientation = orientation.rotate_x()
        orientation = orientation.rotate_z().rotate_z()


ALL_ORIENTATIONS = list(possible_orientations())


def find_common_beacons_helper(
    existing_beacons: set[Vector], scanner: Scanner
) -> Optional[tuple[set[Vector], Vector]]:
    for first_beacon in existing_beacons:
        for orientation in ALL_ORIENTATIONS:
            for second_beacon in scanner.beacons:
                offset = first_beacon - (orientation.multiply_vector(second_beacon))

                second_beacons = set(
                    orientation.multiply_vector(beacon) + offset
                    for beacon in scanner.beacons
                )

                intersection = existing_beacons.intersection(second_beacons)
                if len(intersection) >= 12:
                    return second_beacons, offset

    return None


def find_unique_beacons(scanners: list[Scanner]) -> tuple[set[Vector], list[Vector]]:
    all_beacons = set(scanners[0].beacons)
    offsets = [Vector(0, 0, 0)] * len(scanners)
    queue = deque(scanners[1:])

    while queue:
        scanner = queue.popleft()
        check_response = find_common_beacons_helper(all_beacons, scanner)
        if check_response:
            found_beacons, offset = check_response
            all_beacons = all_beacons.union(found_beacons)
            offsets[scanner.identifier] = offset
        else:
            queue.append(scanner)

    return all_beacons, offsets


def find_max_manhattan_distance(scanners: list[Vector]) -> int:
    max_dist = 0

    for i in range(len(scanners) - 1):
        for j in range(i + 1, len(scanners)):
            max_dist = max(max_dist, (scanners[i] - scanners[j]).manhattan())

    return max_dist


def parse_report(report: str) -> list[Scanner]:
    return [Scanner.parse(scanner) for scanner in report.split("\n\n")]


def first_task(report: str) -> int:
    scanners = parse_report(report)
    beacons, _ = find_unique_beacons(scanners)
    return len(beacons)


def second_task(report: str) -> int:
    scanners = parse_report(report)
    _, scanner_positions = find_unique_beacons(scanners)
    return find_max_manhattan_distance(scanner_positions)
