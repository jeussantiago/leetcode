class NumMatrix:
    '''
    Similar concep to the previous question
    - we want to precaculate the sums in case sumRegion is called many times
    - at any given position, we want to the sum of the rectangle to the top left of the matrix

    __init__

    [
        3,0,1,4,2
        5,6,3,2,1
        1,2,0,1,5
    ]
    sumRegion = [
        3, 3, 4, 8,10
        8,14,18,24,27
        9,17,21,28,36
    ]

    region[curr_pos] = (left + above - diagonal_top_left) + curr_num

    T: O(m * n)
    S: O(m * n)

    sumRegion:

    area of a box at from given indexs = 
        area of total sum up to bottom right given
        minus(-) area of box above
        minus(-) area of box to left
            (they both overlap the box at the top left, so we need to add that back in )
        + area of box at top left

    => Ex:
    topLeft = (1,2) ; botRight = (2,3)
    total = sum(botRight) - sum(botLeft) - sum(topRight) + sum(topLeft)
    total = 28 - 17 - 8 + 3
    total = 6

    T: O(1)
    S: O(m * n)
    '''

    def __init__(self, matrix: List[List[int]]):
        M = len(matrix)
        N = len(matrix[0])
        self.region = [[0] * N for _ in range(M)]

        for row in range(M):
            for col in range(N):
                above_val = self.region[row-1][col] if row > 0 else 0
                top_left_val = self.region[row-1][col -
                                                  1] if row > 0 and col > 0 else 0
                left_val = self.region[row][col-1] if col > 0 else 0

                self.region[row][col] = (
                    above_val + left_val - top_left_val) + matrix[row][col]

    # row1, col1 = top left
    # row2, col2 = bot right
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum_bot_right = self.region[row2][col2]
        sum_bot_left = self.region[row2][col1-1] if col1 - 1 >= 0 else 0
        sum_top_right = self.region[row1-1][col2] if row1 - 1 >= 0 else 0
        sum_top_left = self.region[row1-1][col1 -
                                           1] if row1 - 1 >= 0 and col1 - 1 >= 0 else 0

        return sum_bot_right - sum_bot_left - sum_top_right + sum_top_left


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
