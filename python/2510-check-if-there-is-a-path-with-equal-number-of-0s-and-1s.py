class Solution:
    def isThereAPath(self, grid: List[List[int]]) -> bool:
        '''
        [
            [0,0,0,-3],
            [0,0,0,-2],
            [0,-1,0,-1]
        ]

        n is the len of the rows
        m is the len of the cols
        Time: O(n * m * nm)
            ; (n * m * (nm)) fill the cache the number of possible values
            ;               (nm) is the number of different possible values of total
            (n * m * nm) => (n^2 * m^2)
        Space: O(n * m * nm)
            ; () the number of possible values in the cache
        '''

        ROWS, COLS = len(grid), len(grid[0])
        # number of 0s and 1s in grid is odd, can't reach equality
        if (COLS + ROWS - 1) % 2 == 1:
            return False

        @lru_cache(None)
        def dfs(row, col, total):
            if row >= ROWS or col >= COLS:
                return False

            val = 1 if grid[row][col] == 1 else -1
            total += val
            if row == ROWS - 1 and col == COLS - 1:
                return total == 0

            # go right or go down
            res = dfs(row, col + 1, total) or dfs(row + 1, col, total)
            return res

        return dfs(0, 0, 0)
