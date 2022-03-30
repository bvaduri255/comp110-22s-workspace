"""Dictionary related utility functions."""

__author__ = "730489799"

from csv import DictReader
import csv

# Define your functions below


def read_csv_rows(filename :str) -> list[dict[str, str]]:
    """Read the rows of a csv file into a table."""

    result: list[dict[str, str]] = []

    file_handle = open(filename, "r", encoding = "utf8")
    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)
    
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []

    for row in table:
        item: str = row[column]
        result.append(item)
    
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]

    for column in first_row:
        result[column] = column_values(row_table, column)


    return result


def head(column_table: dict[str, list[str]], num_rows: int) -> dict[str, list[str]]:
    """Returns the first num_rows rows of a column oriented table."""

    result: dict[str, list[str]] = {}


    for item in column_table:
        temp_list: list[str] = []

        for i in range(num_rows):
            temp_list.append(column_table[item][i])

        result[item] = temp_list
    
    return result


def select(column_table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Selected specific columns from a column-oriented table."""
    result: dict[str, list[str]] = {}

    for column in column_names:
        result[column] = column_table[column]
    
    return result


def concat(column_table_1: dict[str, list[str]], column_table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines the entries of two column-oriented tables."""
    result: dict[str, list[str]] = {}

    for column in column_table_1:
        result[column] = column_table_1[column]

    for column in column_table_2:
        if column in result:
            result[column] += column_table_2[column]
        else:
            result[column] = column_table_2[column]
        
    return result


def count(values: list[str]) -> dict[str, int]:
    """Counts the frequencies of values in a given list."""
    result: dict[str, int] = {}

    for value in values:
        if value in result:
            result[value] += 1
        else:
            result[value] = 1
    return result