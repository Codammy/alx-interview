# Island Perimeter Calculation

This project contains a Python function to calculate the perimeter of an island in a grid. 

## Function Description

The `island_perimeter` function takes in a 2D grid of integers, where `1` represents land and `0` represents water. It calculates the perimeter of the island formed by the land cells.

## Usage

To calculate the perimeter of an island in the grid:

```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))  # Output: 12

