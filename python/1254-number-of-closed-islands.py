class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        '''
        - seems like the only islands that aren't considered closed islands (results) are the island connected to the edge of the grid

        - go through the entire grid

        - if found a 0
            - explore all of the connected positions
                - if one of those connected positions is the other edge, then that means that it can't be a closed island
            - if you explore the entire island, and non of the positions is connected to the outer,
                - increase the count of closed islands by 1

        Time: O(m * n)
        Space: O(m * n)
        '''

        ROWS, COLS = len(grid), len(grid[0])
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()

        def isValidPos(row, col):
            return (
                0 <= row < ROWS and
                0 <= col < COLS and
                grid[row][col] == 0 and
                (row, col) not in visited
            )

        def isEdgeLand(row, col):
            return (
                row == 0 or
                row == ROWS - 1 or
                col == 0 or
                col == COLS - 1
            )

        def dfs(row, col):
            isClosedIsland = True
            if isEdgeLand(row, col):
                isClosedIsland = False

            for n_row, n_col, in direction:
                next_row, next_col = row + n_row, col + n_col
                if isValidPos(next_row, next_col):
                    visited.add((next_row, next_col))
                    if not dfs(next_row, next_col):
                        isClosedIsland = False
            return isClosedIsland

        closedIslands = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0 and (row, col) not in visited:
                    visited.add((row, col))
                    if dfs(row, col):
                        closedIslands += 1

        return closedIslands
