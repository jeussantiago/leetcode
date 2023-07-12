class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        '''
        loop:
            - search the matrix until we find the first piece of the island ; == 1
            - when found, search all the positions in the island
            BFS:
                - turn every position into a -1 to show that the position has been visited
                - if it neighbors water, == 0, add to the border list
        before = [              after = [
            [1,1,0,0,0],                    [-1,-1,0,0,0],
            [1,1,0,0,0],                    [-1,-1,0,0,0],
            [0,0,0,0,0],                    [ 0, 0,0,0,0],
            [0,0,0,0,0],                    [ 0, 0,0,0,0],
            [0,0,0,0,1]                     [ 0, 0,0,0,1]
        ]                                ]

        border = [(0,1),(1,0),(1,1)]

        - go to the neighbors of the border
        - if neighbor == -1, visited position
        - if neighbor == 0, unvisited water position
            - add the position into the border queue
            - turn the water position into -1 to show its been visited
        - if neighbor == 1, 2nd island
            - return the number of steps/bridges

        n is the length of the island
        Time: O(n * n)
        Space: O(n * n) ; border queue
        '''
        def borderSearch(island_piece):
            borders = set()
            q = collections.deque([island_piece])
            grid[island_piece[0]][island_piece[1]] = -1
            while q:
                y, x = q.pop()
                # turn the position into -1 to show that its has been visited
                for dy, dx in directions:
                    row, col = y + dy, x + dx
                    if (row < 0 or row >= N or
                                col < 0 or col >= N or
                                grid[row][col] == -1
                            ):
                        # ouut of bounds/ visited position
                        continue

                    # neighbor is water, this makes this position a border position
                    if grid[row][col] == 0:
                        borders.add((y, x))

                    # position can have both water and land neighbors
                    if grid[row][col] == 1:
                        q.appendleft((row, col))
                        grid[row][col] = -1

            return collections.deque(list(borders))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        N = len(grid)
        borders = None
        for row in range(N):
            for col in range(N):
                if grid[row][col] == 1:
                    # found 1st island, search the entire first island for its borders
                    borders = borderSearch((row, col))
                    break

            if borders:
                break

        # search for 2nd island using the borders of first island
        steps = 0
        while borders:
            for _ in range(len(borders)):

                y, x = borders.pop()
                for dy, dx in directions:
                    row, col = y + dy, x + dx
                    if (row < 0 or row >= N or
                                col < 0 or col >= N or
                                grid[row][col] == -1
                            ):
                        # out of bounds/ visited position
                        continue

                    if grid[row][col] == 0:
                        # unvisited possible connection bridge
                        borders.appendleft((row, col))
                        # turn water position into a visited land position
                        grid[row][col] = -1

                    # current piece can be connected to both water and 2nd island
                    if grid[row][col] == 1:
                        return steps

            steps += 1

        return steps
