class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        '''
        - could make the board and fill it in and check constantly
        OR

        - keep a record of the row, column, and diagonal values

        - if you havent founda winner yet
            - if length of moves == 9:
                return Draw
            - otherwise, more moves can still be played
                return 'pending'

        Time: O(1)
            ; the size of the moves array is from the range [0, 9]
        Space: O(1)
            ; there are 3 rows being kept tracked
            ; there are 3 cols being kept tracked
            ; there are 2 diagonals being kept tracked


        0   1    2
        1   2   
        2        0
        '''

        rows = collections.defaultdict(int)
        cols = collections.defaultdict(int)
        negDiag = collections.defaultdict(int)
        posDiag = collections.defaultdict(int)

        player = 1
        for i, move in enumerate(moves):
            player = 1 if i % 2 == 0 else -1

            # update the values
            rows[move[0]] += player
            cols[move[1]] += player
            negDiag[move[0] - move[1]] += player
            posDiag[move[0] + move[1]] += player

            # check if theres a winner
            if (
                abs(rows[move[0]]) == 3 or
                abs(cols[move[1]]) == 3 or
                abs(negDiag[move[0] - move[1]]) == 3 or
                abs(posDiag[move[0] + move[1]]) == 3
            ):

                return 'A' if player == 1 else 'B'

        if len(moves) == 9:
            return 'Draw'
        return 'Pending'
