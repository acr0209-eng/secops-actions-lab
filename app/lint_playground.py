"""Ruff 린트 규칙을 모아 둔 연습 파일입니다."""


def clamp_values(numbers: list[int]) -> list[int]:
    result: list[int] = []
    for value in numbers:
        if 0 < value < 100:
            result.append(value)
    return result


def find_missing(value, items=None):
    if items is None:
        items = []

    if value is None:
        return items

    items.append(value)
    return items