#!/usr/bin/python3
"""
Function that calculates the perimeter of an island in a grid.

The grid is represented as a list of lists, where 1 represents
land and 0 represents water. The function calculates the perimeter
by adding 4 for each land cell and subtracting 2 for each shared edg
e with another land cell.

Args:
    grid (list of list of int): A 2D grid representing the island.

Returns:
    int: The perimeter of the island.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the given grid.

    The perimeter is calculated by adding 4 for each land cell
    and subtracting 2 for each shared edge between adjacent land cells.

    Args:
        grid (list of list of int): A 2D grid representing the island,
        with 1 for land and 0 for water.

    Returns:
        int: The perimeter of the island.
    """
    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4

                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2

                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

    return perimeter
