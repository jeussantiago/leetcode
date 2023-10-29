class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        '''
        - we check for col before row in top_right_diagonal since we will need to check 
        that if we hit a corner and vice versa for bot_left_diagonal

        if direction == top_right_diagonal
            if col == len(mat[0]) - 1
                - increase the row +1
                - keep the same column
                - flip the direction to bot_left_diagonal
            elif row == 0
                - keep row the same
                - increase the column +1
                - flip the direction to bot_left_diagonal
            else
                - decrease row -1
                - increase column +1

        if direction == bot_left_diagonal
            if row == len(mat) - 1
                - keep the same row
                - increase the column +1
                - flip the direcitons to top_right_diagonal
            elif col == 0
                - increase the row +1
                - keep the same column
                - flip the direcitons to top_right_diagonal
            else
                - increase row +1
                - decrease column -1

        - we do this iteration until both row and col are out of bounds in the matrix

        Time: O(m*n)
        Space: O(1)
        '''
        if not mat or not mat[0]:
            return []

        ROWS, COLS = len(mat), len(mat[0])
        row, col = 0, 0
        # direction 1 means top_right_diagonal and direction 0 means bot_left_diagonal
        direction = 1
        res = []
        while row < ROWS and col < COLS:
            res.append(mat[row][col])
            # top_right_diagonal
            if direction:
                if col == COLS - 1:
                    row += 1
                    direction = 0
                elif row == 0:
                    col += 1
                    direction = 0
                else:
                    row -= 1
                    col += 1
            else:
                # bot_left_diagonal
                if row == ROWS - 1:
                    col += 1
                    direction = 1
                elif col == 0:
                    row += 1
                    direction = 1
                else:
                    row += 1
                    col -= 1

        return res
