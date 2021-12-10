BRACKETS_PAIR = {"{": "}", "[": "]", "(": ")", "<": ">"}
SYNTAX_ERROR_SCORE = {")": 3, "]": 57, "}": 1197, ">": 25137}
AUTOCOMPLETE_SCORE = {")": 1, "]": 2, "}": 3, ">": 4}


def syntax_error_score(line: str) -> int:
    stack = []
    for char in line:
        if char in BRACKETS_PAIR:
            stack.append(char)
        else:
            if BRACKETS_PAIR[stack.pop()] != char:
                return SYNTAX_ERROR_SCORE[char]
    return 0


def autocomplete_score(line: str) -> int:
    stack = []
    for char in line:
        if char in BRACKETS_PAIR:
            stack.append(BRACKETS_PAIR[char])
        else:
            stack.pop()

    score = 0
    while stack:
        score = (score * 5) + AUTOCOMPLETE_SCORE[stack.pop()]
    return score


def find_autocomplete_scores(lines: list[str]) -> list[int]:
    return [autocomplete_score(line) for line in lines if syntax_error_score(line) == 0]


def parse_lines(lines_str: str) -> list[str]:
    return lines_str.split()


def first_task(lines_str: str) -> int:
    return sum(syntax_error_score(line) for line in parse_lines(lines_str))


def second_task(lines_str: str) -> int:
    autocomplete_scores = find_autocomplete_scores(parse_lines(lines_str))
    autocomplete_scores.sort()
    return autocomplete_scores[len(autocomplete_scores) // 2]
