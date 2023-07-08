class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
            0 1 2 3 
        0   * 1 1 1
        1   1 2 3 4
        2   1 3 6 10

        - number of unique paths to get to the position in the grid
        - all 0 col and 0 row values are 1
        - values in row and column = value at the [row][col-1] + [row-1][col]
        - in example, number of unique paths to get to row 2, col 3 is 10

        Time: O(m * n)
        Space: O(m * n)
        '''
        grid = [[1] * n for _ in range(m)]
        for row in range(1, m):
            for col in range(1, n):
                grid[row][col] = grid[row-1][col] + grid[row][col-1]

        return grid[-1][-1]
        