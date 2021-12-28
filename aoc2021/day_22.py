from __future__ import annotations
from typing import NamedTuple


def parse_interval(interval: str) -> tuple[int, int]:
    _, values = interval.split("=")
    start_str, end_str = values.split("..")
    return int(start_str), int(end_str)


class Vector(NamedTuple):
    x: int
    y: int
    z: int


class Cuboid(NamedTuple):
    start: Vector
    end: Vector

    def volume(self) -> int:
        s_x, s_y, s_z = self.start
        e_x, e_y, e_z = self.end
        return (e_x - s_x) * (e_y - s_y) * (e_z - s_z)

    def intersect(self, other: Cuboid) -> Cuboid:
        s_x = max(self.start.x, other.start.x)
        s_y = max(self.start.y, other.start.y)
        s_z = max(self.start.z, other.start.z)

        e_x = min(self.end.x, other.end.x)
        e_y = min(self.end.y, other.end.y)
        e_z = min(self.end.z, other.end.z)

        if s_x >= e_x or s_y >= e_y or s_z >= e_z:
            return Cuboid(Vector(0, 0, 0), Vector(0, 0, 0))

        return Cuboid(Vector(s_x, s_y, s_z), Vector(e_x, e_y, e_z))

    @classmethod
    def parse(cls, cuboid: str) -> Cuboid:
        (x_f, x_t), (y_f, y_t), (z_f, z_t) = map(parse_interval, cuboid.split(","))
        return cls(Vector(x_f, y_f, z_f), Vector(x_t + 1, y_t + 1, z_t + 1))


class Step(NamedTuple):
    turn_on: bool
    cuboid: Cuboid

    @classmethod
    def parse(cls, step: str) -> Step:
        action, cuboid = step.split(" ")
        return cls(action == "on", Cuboid.parse(cuboid))


class MutableCuboid:
    def __init__(self, cuboid: Cuboid) -> None:
        self.cuboid = cuboid
        self.off: list[MutableCuboid] = []

    def substract(self, other: MutableCuboid) -> None:
        intersection = self.cuboid.intersect(other.cuboid)
        if intersection.volume() == 0:
            return

        mutable_cuboid = MutableCuboid.from_cuboid(intersection)
        for off_cuboid in self.off:
            off_cuboid.substract(other)

        self.off.append(mutable_cuboid)

    def volume(self) -> int:
        return self.cuboid.volume() - sum(cuboid.volume() for cuboid in self.off)

    @classmethod
    def from_cuboid(cls, cuboid: Cuboid) -> MutableCuboid:
        return cls(cuboid)


def count_turned_on_cubes(steps: list[Step]) -> int:
    cuboids: list[MutableCuboid] = []

    for step in steps:
        mutable_cuboid = MutableCuboid.from_cuboid(step.cuboid)

        for cuboid in cuboids:
            cuboid.substract(mutable_cuboid)

        if step.turn_on:
            cuboids.append(mutable_cuboid)

    return sum(cuboid.volume() for cuboid in cuboids)


def parse_reboot_steps(reboot_steps: str) -> list[Step]:
    return [Step.parse(step) for step in reboot_steps.split("\n")]


def first_task(reboot_steps: str) -> int:
    steps = parse_reboot_steps(reboot_steps)
    bounded_box = Cuboid(Vector(-50, -50, -50), Vector(51, 51, 51))
    initialization_steps = [
        step for step in steps if step.cuboid.intersect(bounded_box) == step.cuboid
    ]
    return count_turned_on_cubes(initialization_steps)


def second_task(reboot_steps: str) -> int:
    steps = parse_reboot_steps(reboot_steps)
    return count_turned_on_cubes(steps)
