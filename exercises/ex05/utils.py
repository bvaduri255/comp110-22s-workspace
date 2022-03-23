"""For functions skeletons and implementations."""

__author__ = "730489799"


def only_evens(listy: list[int]) -> list[int]:
    """Returns a list of only the even elements in a list."""
    out: list[int] = []

    for i in range(len(listy)):
        if listy[i] % 2 == 0:
            out.append(listy[i])

    return out


def sub(listy: list[int], start: int, end: int) -> list[int]:
    """Returns subset of list between given indices."""
    out: list[int] = []
    if start < 0:
        start = 0
    if end >= len(listy):
        end = len(listy)
    for i in range(start, end):
        out.append(listy[i])

    return out


def concat(listy1: list[int], listy2: list[int]) -> list[int]:
    """Concatentate two lists of integers."""
    out: list[int] = []

    for i in range(len(listy1)):
        out.append(listy1[i])

    for i in range(len(listy2)):
        out.append(listy2[i])
    
    return out