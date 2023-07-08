class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        '''
        |1 3 1|     |1 4 5|     |1 4 5|
        |1 5 1|     |2 7 1|     |2 7 6|
        |4 2 1|     |6 2 1|     |6 8 7|

        - work from top left, only moving right or down (connecting squares)
        (can work row by row/left to right since we only care about the values at the current box, left adjacent, and top adjacent)
        - add current box value with the value of the adjacent boxes (top or left box)
            - take the minimum of that value

        Time: O(m * n)
        Space: O(1) 

        '''
        m = len(grid) #row
        n = len(grid[0]) #col

        for row in range(m):
            for col in range(n):
                if row == 0 and col == 0:
                    continue

                left_box_value = grid[row][col-1] if col > 0 else float("inf")
                top_box_value = grid[row-1][col] if row > 0 else float("inf")
                current_value = grid[row][col]
                #replace the current position with the minimum sum
                grid[row][col] = min(current_value + left_box_value, current_value + top_box_value)

        return grid[-1][-1]

