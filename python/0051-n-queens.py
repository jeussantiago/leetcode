class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''
        Brute Force but selective:
        - valid queen location:
            - queens can't be inline horizontal
            - queens can't be inline vertical
            - queens can't be inline diagonal
                - digonals from top left to bottom right are always an increase of 1 row and 1 col
                    - if you subtract the row number from the col number (row - col), it will always be consistent
                    (Q on 0,0 will have diagnoals all valued 0 ; Q on 1,0 will have diagonal valued at 1)
                - diagonals from top right to bottom left are always an increase of 1 row and -1 col
                    - if you add the row number and the col num (row + col), it will always be consistent
                    (Q on 0,3 will have diagonal all valued at 0 ; Q on 0,2 will be valued at 2)
        
        - keep track on invalid queen locations
        (we know that since a queen is invalid if it is in the same row, then we don't need to keep track of that)
        - if a valid location is found
            - place a queen
            - make that location an invalid location
            - call backtrack
            (we need to find all possible solutions/distinct solutions so we need to remove that queen location
            and try another location to see if that works)
            - set queen location back to ".
            - remove the location from the invalid list
        '''
        res = []
        board = [["."] * n for _ in range(n)]
        
        invalid_col = set()
        invalid_top_left_bot_right_diagonal = set() #negative diagonal
        invalid_top_right_bot_left_diagonal = set() #positive diagonal

        def backtrack(row):
            if row == n:
                formatted_board = ["".join(arr) for arr in board]
                res.append(formatted_board)
                return

            for col in range(n):
                #check if the location is a valid location
                if (
                    col in invalid_col or 
                    (row - col) in invalid_top_left_bot_right_diagonal or
                    (row + col) in invalid_top_right_bot_left_diagonal
                ):
                    #skip the invalid location(go to next iteration)
                    continue

                #valid location so add the queen there
                invalid_col.add(col)
                invalid_top_left_bot_right_diagonal.add(row - col)
                invalid_top_right_bot_left_diagonal.add(row + col)
                board[row][col] = "Q"

                #backtrack and find the other valid locations in the next row
                backtrack(row+1)

                #find all possible outcomes so remove the current queen locations
                invalid_col.remove(col)
                invalid_top_left_bot_right_diagonal.remove(row - col)
                invalid_top_right_bot_left_diagonal.remove(row + col)
                board[row][col] = "."
        
        backtrack(0)
        return res
        
        