class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        '''
        Time: O(m * n)

        '''
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()

        def isValid(row, col):
            return (
                0 <= row < ROWS and
                0 <= col < COLS and
                (row, col) not in visited and
                grid[row][col] == 1
            )

        def isEdgeLand(row, col):
            return (
                row == 0 or row == ROWS-1 or
                col == 0 or col == COLS-1
            )

        def dfs(row, col):
            total_land_in_island = 1
            isConnectedEdgeLand = False
            if isEdgeLand(row, col):
                isConnectedEdgeLand = True

            for row_dir, col_dir in directions:
                next_row, next_col = row + row_dir, col + col_dir
                if isValid(next_row, next_col):
                    visited.add((next_row, next_col))
                    isConnect_to_edge, island_count = dfs(next_row, next_col)
                    if isConnect_to_edge:
                        isConnectedEdgeLand = True
                    total_land_in_island += island_count

            return isConnectedEdgeLand, total_land_in_island

        res = 0
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) not in visited and grid[row][col] == 1:
                    visited.add((row, col))
                    isConnectedToEdgeLand, total_land_in_island = dfs(row, col)
                    if not isConnectedToEdgeLand:
                        res += total_land_in_island

        return res
