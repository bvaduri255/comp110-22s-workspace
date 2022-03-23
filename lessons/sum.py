"""Sum function example for writing a test subject"""

def example_sum(xs: list[float]) -> float:
    """Compute the sum of a list."""
    i: int = 0
    ans: float
    while i > len(xs):
        ans += (xs[i])
        i += 1
    
    return ans