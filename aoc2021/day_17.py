from typing import NamedTuple, Generator


class Vector(NamedTuple):
    x: int
    y: int


class Rectangle(NamedTuple):
    bottom_left: Vector
    top_right: Vector

    def __contains__(self, other: object) -> bool:
        if isinstance(other, Vector):
            other_x, other_y = other
            return (
                self.bottom_left.x <= other_x <= self.top_right.x
                and self.bottom_left.y <= other_y <= self.top_right.y
            )
        return False


def trajectory(velocity: Vector) -> Generator[Vector, None, None]:
    curr_x, curr_y = 0, 0
    velocity_x, velocity_y = velocity

    while True:
        yield Vector(curr_x, curr_y)
        curr_x += velocity_x
        curr_y += velocity_y

        velocity_x = max(0, velocity_x - 1)
        velocity_y -= 1


def is_velocity_hits_target_area(velocity: Vector, target_area: Rectangle) -> bool:
    for point in trajectory(velocity):
        if point in target_area:
            return True

        if point.x > target_area.top_right.x or point.y < target_area.bottom_left.y:
            return False

    return False


def velocities_hitting_target(target_area: Rectangle) -> Generator[Vector, None, None]:
    max_x = target_area.top_right.x
    min_y = target_area.bottom_left.y

    for velocity_x in range(1, max_x + 1):
        for velocity_y in range(min_y, -min_y + 1):
            velocity = Vector(velocity_x, velocity_y)
            if is_velocity_hits_target_area(velocity, target_area):
                yield velocity


def parse_range(range_str: str) -> tuple[int, int]:
    _, range_value = range_str.split("=")
    left, right = range_value.split("..")
    return int(left), int(right)


def parse_target_area(area: str) -> Rectangle:
    parts = area.split(" ")
    x_min, x_max = parse_range(parts[2][:-1])
    y_min, y_max = parse_range(parts[3])
    return Rectangle(Vector(x_min, y_min), Vector(x_max, y_max))


def find_velocity_with_highest_position(area: Rectangle) -> Vector:
    return max(velocities_hitting_target(area), key=lambda v: v.y)


def first_task(target_area: str) -> int:
    area = parse_target_area(target_area)
    _, velocity_y = find_velocity_with_highest_position(area)
    return velocity_y * (velocity_y + 1) // 2


def second_task(target_area: str) -> int:
    area = parse_target_area(target_area)
    return sum(1 for _ in velocities_hitting_target(area))
