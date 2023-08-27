class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        '''
        - find adjacent candies
            - vertically and horizontally check the space before, the current space, and the space after
            - can put conditional to check if the space is out of bounds
                - put positions in a set
                    OR
                - turn the values into their negative values - crush the candies


        - Crush the candies (if turn added positions onto set) - needs more space this way
            - go through the set and replace all the numbers with a -1

        - move the above candies downwards
            - iterate from bottom to top
            - if we find a -1, 
                - move empty space pointer to this position
            - if we find a number, 
                - move valuue to empty space pointer
                - decrease pointer position

        m is number of rows
        n is number of columns
        Time: O(m^2 * n^2)
            ; (m * n) find adjacent candies
            ; (m * n) Cursh the candies - turn to -1
            ; (m * n) move candies lower
            ; (m^2 * n^2) repeat steps until can't crush anymore - worst case all the candies get removed
        Space: O(1)
        '''

        ROWS, COLS = len(board), len(board[0])

        def findAdj():
            # find adjacent candies
            isNoAdjConnections = True

            for r in range(ROWS):
                for c in range(COLS):
                    if board[r][c] == 0:
                        continue

                    # Vertical check
                    if (0 < r < ROWS-1) and abs(board[r - 1][c]) == abs(board[r][c]) == abs(board[r + 1][c]):
                        board[r][c] = abs(board[r][c]) * -1
                        board[r - 1][c] = abs(board[r - 1][c]) * -1
                        board[r + 1][c] = abs(board[r + 1][c]) * -1
                        isNoAdjConnections = False

                    if (0 < c < COLS-1) and abs(board[r][c - 1]) == abs(board[r][c]) == abs(board[r][c + 1]):
                        board[r][c] = abs(board[r][c]) * -1
                        board[r][c - 1] = abs(board[r][c - 1]) * -1
                        board[r][c + 1] = abs(board[r][c + 1]) * -1
                        isNoAdjConnections = False

            # crush the candies - turn negatives to 0
            for r in range(ROWS):
                for c in range(COLS):
                    if board[r][c] <= 0:
                        board[r][c] = 0

            return isNoAdjConnections

        # move the above candies downwards
        def drop():
            for c in range(COLS):
                empty_space = -1
                # work from the bottom of board to the top
                for r in range(ROWS-1, -1, -1):
                    if board[r][c] <= 0:
                        empty_space = max(empty_space, r)
                    else:
                        board[r][c], board[empty_space][c] = board[empty_space][c], board[r][c]
                        empty_space -= 1

        while not findAdj():
            drop()

        return board
