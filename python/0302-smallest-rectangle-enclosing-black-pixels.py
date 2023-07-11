class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        '''

        - find the first black square
            - do dfs to explor all positions of the connected black square
                - keep a visited set to make sure you don't go over repeated squares
                - at each position,
                    - keep a record of the
                        : min col, max col
                        : min row, max row

        Time: O(m * n)
        Space: O(m * n) b/c of the visited set

        - for loop is the same as dfs since the entire matrix could be visited, 
        - in this case howeverr, we don't need to keep a visited so it saves space
        - although this algorithm has the same time compelxity as the dfs solution,
        - it is slower if not all positions are black

        Time: O(m * n)
        Space: O(1)
        '''
        x_range = [float('inf'), float('-inf')]
        y_range = [float('inf'), float('-inf')]

        def updateBoundaries(row, col):
            x_range[0] = min(x_range[0], col)
            x_range[1] = max(x_range[1], col)

            y_range[0] = min(y_range[0], row)
            y_range[1] = max(y_range[1], row)

        for i, row in enumerate(image):
            for j, c in enumerate(row):
                if c == "1":
                    updateBoundaries(i, j)

        w = x_range[1] - x_range[0] + 1
        h = y_range[1] - y_range[0] + 1

        return w * h
