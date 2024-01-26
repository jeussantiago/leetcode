class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        '''
        k is the number of moves
        Time: O(m * n * k)
        Space: O(m * n * k)
            ; cache - all possible operations
        '''
        MOD = 10 ** 9 + 7
        cache = {}

        def dfs(row, col, movesLeft):
            if row < 0 or row >= m or col < 0 or col >= n:
                return 1

            if movesLeft == 0:
                return 0

            if (row, col, movesLeft) in cache:
                return cache[(row, col, movesLeft)]

            cache[(row, col, movesLeft)] = (
                dfs(row + 1, col, movesLeft - 1) +
                dfs(row - 1, col, movesLeft - 1) +
                dfs(row, col + 1, movesLeft - 1) +
                dfs(row, col - 1, movesLeft - 1)
            ) % MOD

            return cache[(row, col, movesLeft)]

        return dfs(startRow, startColumn, maxMove)
