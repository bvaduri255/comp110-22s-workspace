"""Test cases for the functions in the util file."""

__author__ = "730489799"

from utils import only_evens, sub, concat


def test_only_evens_case1() -> None:
    """Tests the only_evens function if the list is a mix of evens and odds."""
    xs: list[int] = [1, 4, 3, 2, 3, 4]
    assert only_evens(xs) == [4, 2, 4]


def test_only_evens_case2() -> None:
    """Tests if all elements in the input list are odd; should return empty list."""
    xs: list[int] = [1, 5, 3, 3, 9, 7]
    assert only_evens(xs) == []


def test_only_evens_case3() -> None:
    """Tests if the input list is empty. Since there are no elements."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_sub_case1() -> None:
    """Tests if the list is a list of more than 2 elements. Regular test case."""
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7]
    left: int = 3
    right: int = 6
    assert sub(xs, left, right) == [4, 5, 6]


def test_sub_case2() -> None:
    """Tests if the left bound is negative and the right bound is beyond the length of the list."""
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7]
    left: int = -2
    right: int = 30
    assert sub(xs, left, right) == [1, 2, 3, 4, 5, 6, 7]


def test_sub_case3() -> None:
    """Tests if the start and end are the same index. Should return an empty list."""
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7]
    left: int = 3
    right: int = 3
    assert sub(xs, left, right) == []


def test_concat_case1() -> None:
    """Tests if one list is empty. Should return the non-empty list."""
    xs1: list[int] = [1, 2, 3, 4, 5, 6]
    xs2: list[int] = []
    assert concat(xs1, xs2) == [1, 2, 3, 4, 5, 6]


def test_concat_case2() -> None:
    """Tests as regular case with two non-empty lists."""
    xs1: list[int] = [1, 3, 5, 7, 9]
    xs2: list[int] = [2, 4, 6, 8, 10]
    assert concat(xs1, xs2) == [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]


def test_concat_case3() -> None:
    """Tests if both lists are empty. Should return empty list."""
    xs1: list[int] = []
    xs2: list[int] = []
    assert concat(xs1, xs2) == []