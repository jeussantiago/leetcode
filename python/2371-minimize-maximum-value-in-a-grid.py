class Solution:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:
        '''
        2 4 5 => 1 2 3 == 1 2 3
        7 3 9    2 1 4    3 1 4

        - store the largest value for each row
        - store the largest value for each col

        - store (val, row, col) in a minHeap

        heap = [(2,0,0),(3,1,1),(4,0,1),(5,0,2),(7,1,0),(9,1,2)]

        row_max_value = [0,0]
        col_max_value = [0,0,0]

        - pop from the heap
        (2,0,0)
        - get the max value value from the row and col 
            max(row_max_value[curr_row], col_max_value[curr_col])
            - set this value to the position in the matrix + 1
            - update the col max_val at col pos, same with row

        n is row length
        m is col length
        Time: O(nm * log(nm))
            ; (n * m) add all items to heap

            ; (n * m) iterate through entire heap until its empty (this is same as iterating through grid)
            ; (log(nm)) pop from heap
            ; (1) update grid value and variables
            => (n * m + (nm * logn(nm) + 1))

        Space: O(n * m)
            ; (n * m) heap
            ; (n) row storage
            ; (m) col storage
            => (nm + n + m)
        '''

        N, M = len(grid), len(grid[0])  # row, col

        rowMax = collections.defaultdict(int)
        colMax = collections.defaultdict(int)
        minHeap = []
        for row in range(N):
            for col in range(M):
                heappush(minHeap, (grid[row][col], row, col))

        while minHeap:
            _, row, col = heappop(minHeap)
            val = max(rowMax[row], colMax[col]) + 1
            # update row, col, and grid

            grid[row][col] = val
            rowMax[row] = val
            colMax[col] = val

        return grid
