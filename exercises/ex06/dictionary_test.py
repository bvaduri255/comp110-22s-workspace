"""Test cases for the functions in the dictionary file."""

__author__ = "730489799"

from dictionary import invert, favorite_color, count


def test_invert_case1() -> None:
    """Tests a regular case for the invert function."""
    xs: dict[str, str] = {"Hello": "Hi", "Goodbye": "Bye", "A": "1"}
    xs_invert: dict[str, str] = {"Hi": "Hello", "Bye": "Goodbye", "1": "A"}
    assert invert(xs) == xs_invert
    

def test_invert_case2() -> None:
    """Tests another regular given case for the invert function."""
    xs: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    xs_invert: dict[str, str] = {'z': 'a', 'y': 'b', 'x': 'c'}
    assert invert(xs) == xs_invert


def test_invert_case3() -> None:
    """Test the empty case to see if the function can invert an empty dictionary."""
    xs: dict[str, str] = {}
    xs_invert: dict[str, str] = {}
    assert invert(xs) == xs_invert


def test_favorite_color_case1() -> None:
    """Tests for the given case for the favorite color function."""
    xs: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    fav_col: str = "blue"
    assert favorite_color(xs) == fav_col


def test_favorite_color_case2() -> None:
    """Tests another regular case for the favorite color function."""
    xs: dict[str, str] = {"Alice": "Orange", "Bob": "Blue", "Carol": "Yellow", "David": "Orange", "Earl": "Orange"}
    fav_col: str = "Orange"
    assert favorite_color(xs) == fav_col


def test_favorite_color_case3() -> None:
    """Tests for empty dictionary case for the favorite color function."""
    xs: dict[str, str] = {}
    fav_col: str = ""
    assert favorite_color(xs) == fav_col


def test_count_case1() -> None:
    """Tests using regular case for the color function."""
    xs: list[str] = ["1", "2", "2", "2", "3"]
    ans: dict[str, int] = {"1": 1, "2": 3, "3": 1}
    assert count(xs) == ans


def test_count_case2() -> None:
    """Tests using same second case as favorite color."""
    xs: list[str] = ["A", "A", "B", "C", "D", "E"]
    ans: dict[str, int] = {"A": 2, "B": 1, "C": 1, "D": 1, "E": 1}
    assert count(xs) == ans


def test_count_case3() -> None:
    """Tests for empty dictionary to see if the count will return zero."""
    xs: list[str] = []
    ans: dict[str, int] = {}
    assert count(xs) == ans