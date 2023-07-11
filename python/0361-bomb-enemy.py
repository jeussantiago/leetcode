class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        '''
        Dynamic Programming:

        - at each row, calculate the number of hits on the row
            - if encounter a wall, re-calculate the number of hits until reach a wall or the end

        - at each col, calculate the number of hits on the col
            - if encounter a wall, re-calculate the number of hits until reacha  wall or the end
        - store the col, hits in a dp b/c we need to keep track of all the cols as we go through each cell
        - don't need to do this for rows since we go through rows in the outer loop

        W is the width of the grid
        H is the height of the grid
        Time: O(W * H) ; we go to each 3 at most 3 times
                       ;    - once for just visiting the cell
                       ;    - once for calculating the hits on rows
                       ;    - once for calculating the hits on cols
                       ; O(3 * W * H)
        Space: O(W) ; only extra space usage is for the cols dp array
        '''
        H, W = len(grid), len(grid[0])

        def hitsOnRow(row, colStart):
            row_hits = 0
            for col in range(colStart, W):
                if grid[row][col] == "W":
                    return row_hits
                elif grid[row][col] == "E":
                    row_hits += 1

            return row_hits

        def hitsOnCol(rowStart, col):
            col_hits = 0
            for row in range(rowStart, H):
                if grid[row][col] == "W":
                    return col_hits
                elif grid[row][col] == "E":
                    col_hits += 1

            return col_hits

        res = 0
        row_hits, col_hits = 0, [0] * W
        for row in range(H):
            for col in range(W):

                # calculate the number of hits on this row until the wall or the end of row
                if col == 0 or grid[row][col-1] == "W":
                    row_hits = hitsOnRow(row, col)
                    # print('hitsOnRow:', row, col, '|||', row_hits)

                # calculate the number of hits on this col until the wall or the end of col
                if row == 0 or grid[row-1][col] == "W":
                    col_hits[col] = hitsOnCol(row, col)
                    # print('hitsOnCol:', row, col, '|||', col_hits)

                # calculate total hits for an empty cell
                if grid[row][col] == "0":
                    total_hits = row_hits + col_hits[col]
                    res = max(res, total_hits)

        return res
