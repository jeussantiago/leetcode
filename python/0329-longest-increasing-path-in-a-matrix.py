class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        '''
        - for a pos in the matrix, find the longest path

        - if the pos has been visited
            - go to cache, and see what the longest path is in the graph

        - if pos has not been visited
            - find the longest path
            - go to its neighbors, only dfs if it is a valid position within the graph (within boundaries)

        Time: O(m * n)
        Space: O(m * n)
        '''
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}

        def isValidPos(row, col):
            return (
                0 <= row < ROWS and
                0 <= col < COLS
            )

        def dfs(row, col):
            if (row, col) in cache:
                return cache[(row, col)]

            longestPath = 1
            for row_dir, col_dir in directions:
                next_row, next_col = row + row_dir, col + col_dir
                if isValidPos(next_row, next_col) and matrix[next_row][next_col] > matrix[row][col]:
                    longestPath = max(longestPath, dfs(next_row, next_col) + 1)

            cache[(row, col)] = longestPath
            return longestPath

        longest_path = 1
        for row in range(ROWS):
            for col in range(COLS):
                longest_path = max(longest_path, dfs(row, col))

        return longest_path
