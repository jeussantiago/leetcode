class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        '''
        Time: O(m * n)
        Space: O(m + n)
        '''
        ROWS, COLS = len(grid), len(grid[0])
        rowDp, colDp = [0] * ROWS, [0] * COLS
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col]:
                    rowDp[row] += 1
                    colDp[col] += 1
                else:
                    rowDp[row] -= 1
                    colDp[col] -= 1

        for row in range(ROWS):
            for col in range(COLS):
                # we can use the given matrix to save space
                grid[row][col] = rowDp[row] + colDp[col]

        return grid
