class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        '''
        - store positions of 0s initially in queue

        - run through q
            - if neighbor is a 0 or is visited, don't continue
            (0 positions are already going to be in visited so dont need to check if its 0)
            - if neighbor is a 1, at the position in the matrix, we put +1 our current value

        Time: O(m * n)
            ; run through the matrix twice
        Space: O(m * n)
            ; space for queue
            ; visited set
        '''
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(mat), len(mat[0])
        visited = set()
        q = collections.deque([])
        for row in range(ROWS):
            for col in range(COLS):
                if mat[row][col] == 0:
                    q.appendleft((row, col))
                    visited.add((row, col))

        res = [[0] * COLS for _ in range(ROWS)]

        while q:
            row, col = q.pop()
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if (
                    new_row < 0 or new_row >= ROWS or
                    new_col < 0 or new_col >= COLS or
                    (new_row, new_col) in visited
                ):
                    continue

                res[new_row][new_col] = res[row][col] + 1
                q.appendleft((new_row, new_col))
                visited.add((new_row, new_col))

        return res
