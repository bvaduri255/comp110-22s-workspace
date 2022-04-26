"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = """730489799"""


class Simpy:
    """Class for numpy clone object."""
    values: list[float]

    def __init__(self, listy: list[float]) -> None:
        """Initialize simpy object."""
        self.values = listy

    def __str__(self) -> str:
        """Print out simpy as string object that is readable."""
        out: str = "Simpy(" + str(self.values) + ")"
        return out

    def fill(self, value: float, num: int) -> None:
        """Fill simpy object with a certain number of the same value."""
        self.values = []

        while num:
            self.values.append(value)
            num -= 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill simpy object with arithmetic sequence of values."""
        assert step != 0.0
        self.values = []
        while start != stop:
            self.values.append(start)
            start += step

    def sum(self) -> float:
        """Add values in simpy object."""
        return sum(self.values)    

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Addition operator overload for simpy objects."""
        result: Simpy = Simpy([])
        if type(rhs) is float:
            for i in range(len(self.values)):
                result.values.append(self.values[i] + rhs)
        
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] + rhs.values[i])
        
        return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Exponential operator overload for simpy objects."""
        result: Simpy = Simpy([])
        if type(rhs) is float:
            for i in range(len(self.values)):
                result.values.append(self.values[i] ** rhs)
        
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] ** rhs.values[i])
        
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Equality operator overload for simpy object."""
        result: list[bool] = []
        if type(rhs) is float:
            for i in range(len(self.values)):
                result.append(self.values[i] == rhs)
        
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] == rhs.values[i])
        
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Greater than inequality operator for simpy objects."""
        result: list[bool] = []
        if type(rhs) is float:
            for i in range(len(self.values)):
                result.append(self.values[i] > rhs)
        
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] > rhs.values[i])
        
        return result
        
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Subscript operator overload for simpy objects."""
        if type(rhs) is int:
            return self.values[rhs]
        result: Simpy = Simpy([])
        if type(rhs) is list:
            for i in range(len(rhs)):
                if rhs[i]:
                    result.values.append(self.values[i])
        
        return result