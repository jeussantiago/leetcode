class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ''' 
        bottom up BFS:

        - go to the very end,
        - if reached the bottom right, return 0
            - if not, return -1

        - if the return value is >= 0
            - add 1 step for north, south, east, west directions
            - add 2 steps for diagonal directions

        - keep the minimum step path to the corner,
        - save that minimum to the cache

        [0,0,0]
        [1,0,0]
        [1,1,0]

        Time: O(n * n) ; visiting each cell once
        Space: O(n) 
                ; no extra space used for solution, overwriting input
                ; extra spaced used for queue
        '''
        def isValid(row, col):
            if (
                0 <= row < N and
                0 <= col < N and
                grid[row][col] == 0
            ):
                return True

            return False

        if grid[0][0] == 1 or grid[-1][-1]:
            return -1
        grid[0][0] = 1

        N = len(grid)
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),  # compass step directions
            (1, 1), (-1, 1), (-1, -1), (1, -1)  # diagonal step directions
        ]

        q = collections.deque([(0, 0)])
        while q:
            r, c = q.pop()

            if (r, c) == (N-1, N-1):
                return grid[-1][-1]

            for dr, dc in directions:
                row, col = dr + r, dc + c
                if isValid(row, col):
                    q.appendleft((row, col))
                    grid[row][col] = grid[r][c] + 1

        return -1
