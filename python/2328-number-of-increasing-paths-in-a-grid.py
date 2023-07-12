class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        '''
        9 8 7 8     1 3 7 1
        8 9 8 1     3 1 2 4

        1 3 0 0 
        0 1 0 0

        7, 7-8, 7-8-9, 7-8-9 : 3 from left ; 2 from bot

        DFS

        if next pos in visited:
            - add the count to our count
        if next pos out of bounds:
            - don't do anything (+ 0)

        Time: O(m * n)
        Space: O(m * n)
        '''

        MOD = 10 ** 9 + 7
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        dp = [[0] * COLS for _ in range(ROWS)]

        def dfs(row, col):
            if dp[row][col] != 0:
                return dp[row][col]

            dp[row][col] = 1

            for dr, dc in directions:
                n_row, n_col = row + dr, col + dc
                if (
                    0 <= n_row < ROWS and
                    0 <= n_col < COLS and
                    grid[n_row][n_col] > grid[row][col]
                ):
                    dp[row][col] += (dfs(n_row, n_col) % MOD)

            return dp[row][col]

        res = 0
        for row in range(ROWS):
            for col in range(COLS):
                res += dfs(row, col)

        return res % MOD
