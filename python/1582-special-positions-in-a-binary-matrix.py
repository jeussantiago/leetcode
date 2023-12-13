class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        '''
        Time: O(m * n)
        Space: O(m + n)
        '''
        ROWS, COLS = len(mat), len(mat[0])
        rowDp, colDp = [0] * ROWS, [0] * COLS

        # fill the appearances of the 1s
        for row in range(ROWS):
            for col in range(COLS):
                if mat[row][col] == 1:
                    rowDp[row] += 1
                    colDp[col] += 1

        # get the number of special positions
        special_pos_cnt = 0
        for row in range(ROWS):
            for col in range(COLS):
                if (
                    mat[row][col] == 1
                    and rowDp[row] == 1
                    and colDp[col] == 1
                ):
                    special_pos_cnt += 1

        return special_pos_cnt
