"""For functions skeletons and implementations."""

__author__ = "730489799"


def invert(hmap: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values of a dictionary."""
    output: dict[str, str] = {}
    for item in hmap:
        for val in output:
            if hmap[item] == val:
                raise KeyError
        output[hmap[item]] = item
    
    return output


def favorite_color(hmap: dict[str, str]) -> str:
    """Prints most common color in dictionary."""
    freq: dict[str, int] = {}
    max_val: int = 0
    for item in hmap:
        color: str = hmap[item]
        if color in freq:
            freq[color] += 1
            max_val = max(max_val, freq[color])
        else:
            freq[color] = 1
            max_val = max(max_val, freq[color])
    
    for item in freq:
        if freq[item] == max_val:
            return item
    
    return ""


def count(listy: list[str]) -> dict[str, int]:
    """Returns the frequency of occurences of values in a list."""
    freq: dict[str, int] = {}
    for item in listy:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq