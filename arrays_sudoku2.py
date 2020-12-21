"""
Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers in such a way that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid all contain all of the numbers from 1 to 9 one time.

Implement an algorithm that will check whether the given grid of numbers represents a valid Sudoku puzzle according to the layout rules described above. Note that the puzzle represented by grid does not have to be solvable.

Example

For

grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
the output should be
sudoku2(grid) = true;

"""
import collections
import numpy as np
def sudoku2(grid):
    grid = np.array(grid)
    for i in range(len(grid)):
        row_count = False
        col_count = False
        sub_count = False
        row = collections.Counter((grid[i]))
        col = collections.Counter((grid.T[i]))
        i,j = (i//3)*3, (i%3)*3
        sub = collections.Counter((grid[i:i+3, j:j+3].ravel()))
        del row['.']
        del col['.']
        del sub['.']
        if row:
            row_count = max(row.values()) > 1
        if col:
            col_count = max(col.values()) >1
        if sub:
            sub_count = max(sub.values()) >1
        if row_count or col_count or sub_count:
            return False
    return True 
