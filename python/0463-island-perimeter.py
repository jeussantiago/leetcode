class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        '''
        DFS

        - if out of bounds or water
            (+1) perimeter
        -  if visited
            (-1) perimeter

        n is the number of rows
        m is the number of cols
        Time: O(n * m)
        Space: O(n * m)
            ; recursion stack worst case is visiting every node
        '''

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(row, col):
            if (
                row < 0 or row >= ROWS or
                col < 0 or col >= COLS or
                grid[row][col] == 0
            ):
                return 1

            if (row, col) in visited:
                return 0

            visited.add((row, col))

            perimeter = 0
            for dc, dr in directions:
                perimeter += dfs(row + dr, col + dc)

            return perimeter

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    return dfs(row, col)
