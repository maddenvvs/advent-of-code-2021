from __future__ import annotations


class Board:
    numbers: list[list[int]]
    numbers_sum: int
    marked_sum: int
    positions: dict[int, tuple[int, int]]

    def __init__(self, numbers: list[list[int]]):
        self.numbers = numbers
        self.numbers_sum = 0
        self.marked_sum = 0
        self.positions = {}

        for i, row in enumerate(numbers):
            for j, num in enumerate(row):
                self.numbers_sum += num
                self.positions[num] = (i, j)

    def self_score(self) -> int:
        return self.numbers_sum - self.marked_sum

    def mark(self, number: int) -> None:
        position = self.positions.get(number, None)
        if position is None:
            return

        row, col = position
        self.marked_sum += number
        self.numbers[row][col] = -1

    def is_won(self) -> bool:
        for row in self.numbers:
            if all(n == -1 for n in row):
                return True

        for col in zip(*self.numbers):
            if all(n == -1 for n in col):
                return True

        return False

    @classmethod
    def parse(cls, board_text: str) -> Board:
        numbers = [list(map(int, line.split())) for line in board_text.split("\n")]
        return cls(numbers)


class Bingo:
    def __init__(self, boards: list[Board]):
        self.boards = boards

    def mark(self, number: int) -> None:
        for board in self.boards:
            board.mark(number)

    def find_winning_boards(self) -> list[Board]:
        return [board for board in self.boards if board.is_won()]

    def remove_boards(self, boards: list[Board]) -> None:
        for board in boards:
            self.boards.remove(board)

    @property
    def boards_count(self) -> int:
        return len(self.boards)

    @classmethod
    def parse(cls, boards_text: str) -> Bingo:
        boards_list = [Board.parse(b) for b in boards_text.split("\n\n")]
        return cls(boards_list)


class Simulation:
    def __init__(self, game: Bingo, drawn_numbers: list[int]):
        self.game = game
        self.drawn_numbers = drawn_numbers

    def find_kth_winning_score(self, kth: int) -> int:
        for num in self.drawn_numbers:
            self.game.mark(num)
            winning_boards = self.game.find_winning_boards()
            if kth <= len(winning_boards):
                board = winning_boards[kth - 1]
                return board.self_score() * num
            self.game.remove_boards(winning_boards)
            kth -= len(winning_boards)

        return 0

    def find_first_winning_score(self) -> int:
        return self.find_kth_winning_score(1)

    def find_last_winning_score(self) -> int:
        return self.find_kth_winning_score(self.game.boards_count)

    @classmethod
    def parse(cls, game_text: str) -> Simulation:
        delimiter_pos = game_text.find("\n\n")
        drawn_numbers = [int(i) for i in game_text[:delimiter_pos].split(",")]
        game = Bingo.parse(game_text[delimiter_pos + 2 :])
        return cls(game, drawn_numbers)


def first_task(bingo_game_text: str) -> int:
    simulation = Simulation.parse(bingo_game_text)
    return simulation.find_first_winning_score()


def second_task(bingo_game_text: str) -> int:
    simulation = Simulation.parse(bingo_game_text)
    return simulation.find_last_winning_score()
