class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        - starting from the borders of the atlantic ocean, 
        BFS or dfs the neighbors of the current cell/border
            - condition:
                - the neighbor has not been visited
                - the neighbor has a higher value than the current cell

        - in this way, we will be able to see all the positions that water can possibly flow and reach the atlantic ocean

        - now just do the same for the pacific ocean
            - if they share positions
                - that means water can flow to the atlantic and pacific
                from this cell position

        edge case:
        - a large majority of the middle is the same height
            - this means that we can't stop searching until we find a dip in the height

        [1, 1, 3, 3, 3]
        [1, 3, 3, 3, 3]
        [3, 3, 3, 3, 3]
        [3, 3, 3, 3, 1]
        [3, 3, 3, 1, 1]

        m is the number of rows
        n is the number of columsn
        Time: O(m * n)
        Space: O(m * n) ; atlantic and pacific visited set

        '''
        m, n = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(land):
            visited = set(land)
            while land:
                y, x = land.pop()
                for dy, dx in directions:
                    row, col = y + dy, x + dx
                    if (
                        row < 0 or row >= m or
                        col < 0 or col >= n or
                        (row, col) in visited or
                        heights[row][col] < heights[y][x]
                    ):
                        continue

                    land.appendleft((row, col))
                    visited.add((row, col))

            return visited

        atlantic_borders = collections.deque([])
        for row in range(m):
            atlantic_borders.append((row, n-1))
        for col in range(n-1):
            atlantic_borders.append((m-1, col))

        pacific_borders = collections.deque([])
        for col in range(n):
            pacific_borders.append((0, col))
        for row in range(1, m):
            pacific_borders.append((row, 0))

        # visit all cells that are higher which allow water to flow into the atlantic an dpacific
        atlantic_reach = bfs(atlantic_borders)
        pacific_reach = bfs(pacific_borders)

        return atlantic_reach.intersection(pacific_reach)
