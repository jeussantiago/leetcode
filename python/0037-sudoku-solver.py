class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        
        - check if a number is valid
            - check all values of column
            - check all values of row
            - check all values of a block => [3*(row//3) + i//3][3*(col//3) + i%3] => where i is the range(9)
                - check all members of upper, then middle, then bottom row in order first. thats why row uses i//3 and col useds i%3
        
        - backtracking
            - go through all positions in a board => 2 loops for row and column
            - go through all possible numbers that can be placed in the available slot
                - available slot = '.'
            - check if the entered number is valid (make function)
            - if valid => 
                - replace the '.' with the number
                - call backtracking with the new board b/c want to test all numbers
            - False if went through all numbers and nothing is possible
            

        """
        # backtracking helper
        def solve(board):
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        for num in range(1,10):
                            num = str(num) # moved from inside isValid because we need to replace the value of '.' with the same type
                            if isValid(board, row, col, num):
                                board[row][col] = num
                                if solve(board):
                                    return True
                                board[row][col] = '.'
                        return False
            return True


        # checks if a number is valid
        def isValid(board, row, col, num):
            for i in range(9):
                if (
                    board[i][col] == num or
                    board[row][i] == num or
                    board[3*(row//3) + i//3][3*(col//3) +i%3] == num
                ):
                    return False
            return True


        solve(board)

        
















