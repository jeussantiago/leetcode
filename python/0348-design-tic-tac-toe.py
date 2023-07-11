class TicTacToe:
    '''
    To Win:
        - entire horizontal row needs to be the same
        - entire vertical columne needs to be the same
        - entire long positive diagonal needs to be the same
        - entire long negative diagonal needs to be the same

    - keep track of the totals of each: player 1= 1 ; player 2=-1 
    (running total)
        - row (n size)
        - col (n size)
        - positive diagonal (theres only 1 positive diagonal so can just be an int)
            - (3,0) (2,1) (1,2) (0,3) ; n=4
            - col == n - row - 1
        - negative diagonal (theres only 1 negative diagonal so can just be an int)
            - row == col

    if the total == n
        - this means that an entire row/col/or diagonal is filled with only the same player value
        - this player has won

    __init__:
    T: O(1)
    S: O(1)

    move:
    T: O(1)
    S: O(n + n) row and col list
     : O(n)

    | 2 2 |
    | _ 1 |
    '''

    def __init__(self, n: int):
        self.rows = [0] * n
        self.cols = [0] * n
        self.pos_diag = 0
        self.neg_diag = 0

    def move(self, row: int, col: int, player: int) -> int:
        n = len(self.cols)

        player_val = 1 if player == 1 else -1

        self.rows[row] += player_val
        self.cols[col] += player_val

        # negative diagonal
        if row == col:
            self.pos_diag += player_val

        # positive diagonal
        if col == n - row - 1:
            self.neg_diag += player_val

        # check if full row, col, diag exist => means a player has won
        if (
            abs(self.rows[row]) == n or
            abs(self.cols[col]) == n or
            abs(self.pos_diag) == n or
            abs(self.neg_diag) == n
        ):
            return player

        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
