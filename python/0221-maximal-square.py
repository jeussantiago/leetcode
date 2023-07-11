class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        '''
        Recursion

        - we need to check ___ of index
            - right
            - below
            - bottom right (diagonal)

        - each position will tell us the largest square it can make
        - if the position is a "0"
            - then save 0 in the cache for the position
        - if its a "1"
            - we can look to the other right, below, and diag positions
            - the minimum value between those 3 tells us that we can make a square with that min position,
            - if you include the current index, that we can add 1 to the size of the square

        Matrix          Cache
        1 0 1 1         1 0 1 1 0
        1 1 0 1  =>     2 1 0 1 0 
        1 1 0 1         1 1 0 1 0
                        0 0 0 0 0

        - the biggest square a position can make is in the cache
        return max(cache.values())

        Time: O(m*n)
        Space: O(m*n)

        '''
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}

        def helper(r, c):
            if r >= ROWS or c >= COLS:
                return 0

            if (r, c) not in cache:
                down = helper(r+1, c)
                diag = helper(r+1, c+1)
                right = helper(r, c+1)

                cache[(r, c)] = 0
                if matrix[r][c] == "1":
                    cache[(r, c)] = 1 + min(right, diag, down)

            return cache[(r, c)]

        helper(0, 0)
        return max(cache.values())**2
