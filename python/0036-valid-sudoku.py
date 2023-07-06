class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        Hash set
        - create a dictionary for the rows, cols, and blocks to keep track of the numbers in them
        - go through all rows
        - if a number already exist in that location, its not a valid dictionary

        Time: O(9^2)
        Space: O(9^2)
        '''
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        block = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                #skip empty spaces in sudoku
                if board[r][c] == '.':
                    continue
                #check if the number is in the row, col, and block
                if (
                    board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in block[(r//3, c//3)]
                ):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                block[(r//3, c//3)].add(board[r][c])
        return True





