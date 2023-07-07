class Solution:
    def totalNQueens(self, n: int) -> int:
        '''
        Literally the same problem as 51. N-Queens
        - just return the length of the res
        '''
        res = 0
        board = [["."] * n for _ in range(n)]

        invalid_col = set()
        invalid_top_left_bot_right_diagonal = set() #negative diagonal (row - col)
        invalid_top_right_bot_left_diagonal = set() #positive diagonal (row + col)


        def backtrack(row):
            if row == n:
                #key word - not referring to local variable called "res"
                nonlocal res 
                res += 1
                return

            #go through the cols
            for col in range(n):
                #check if location is valid
                if (
                    col in invalid_col or
                    (row - col) in invalid_top_left_bot_right_diagonal or
                    (row + col) in invalid_top_right_bot_left_diagonal
                ):
                    #skip if invalid
                    continue
                
                #add location as invalid location
                invalid_col.add(col)
                invalid_top_left_bot_right_diagonal.add(row - col)
                invalid_top_right_bot_left_diagonal.add(row + col)
                board[row][col] = 'Q'

                #backtrack
                backtrack(row + 1)

                #all possible configurations - remove location as invalid
                invalid_col.remove(col)
                invalid_top_left_bot_right_diagonal.remove(row - col)
                invalid_top_right_bot_left_diagonal.remove(row + col)
                board[row][col] = '.'
        
        backtrack(0)
        return res
