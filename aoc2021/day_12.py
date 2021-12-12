from __future__ import annotations
from collections import defaultdict

START_CAVE_NAME = "start"
FINISH_CAVE_NAME = "end"


class CavesMap:
    def __init__(self, graph: dict[str, list[str]]) -> None:
        self.graph = graph

    def count_distinct_paths_of_first_type(self) -> int:
        visited = set((START_CAVE_NAME,))
        return self.count_paths_of_first_type(START_CAVE_NAME, visited)

    def count_paths_of_first_type(self, cave: str, visited: set[str]) -> int:
        if cave == FINISH_CAVE_NAME:
            return 1

        paths_count = 0

        for neighbour in self.graph[cave]:
            if neighbour in visited:
                continue
            if neighbour.islower():
                visited.add(neighbour)
                paths_count += self.count_paths_of_first_type(neighbour, visited)
                visited.remove(neighbour)
            else:
                paths_count += self.count_paths_of_first_type(neighbour, visited)

        return paths_count

    def count_distinct_paths_of_second_type(self) -> int:
        visited: dict[str, int] = defaultdict(int)
        visited[START_CAVE_NAME] += 1
        return self.count_paths_of_second_type(START_CAVE_NAME, visited, False)

    def count_paths_of_second_type(
        self, cave: str, visited: dict[str, int], has_two: bool
    ) -> int:
        if cave == FINISH_CAVE_NAME:
            return 1

        paths_count = 0

        for neighbour in self.graph[cave]:
            if neighbour == START_CAVE_NAME:
                continue
            if has_two and visited[neighbour] > 0:
                continue

            if neighbour.isupper():
                paths_count += self.count_paths_of_second_type(
                    neighbour, visited, has_two
                )
            else:
                visited[neighbour] += 1
                paths_count += self.count_paths_of_second_type(
                    neighbour, visited, has_two or visited[neighbour] == 2
                )
                visited[neighbour] -= 1

        return paths_count

    @classmethod
    def parse(cls, caves: str) -> CavesMap:
        caves_map = defaultdict(list)
        for tunnel in caves.split("\n"):
            start, end = tunnel.split("-")
            caves_map[start].append(end)
            caves_map[end].append(start)
        return cls(caves_map)


def first_task(caves: str) -> int:
    caves_map = CavesMap.parse(caves)
    return caves_map.count_distinct_paths_of_first_type()


def second_task(caves: str) -> int:
    caves_map = CavesMap.parse(caves)
    return caves_map.count_distinct_paths_of_second_type()
