class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        - make a deepcopy of the original which will be iterated over to check if a position needs to be change

        Time: O(m * n)
        Space: O(m * n)

        FOLLOW UP QUESTIONS ARE NICE TO PRACTICE BECAUSE THEY FOCUS ON SCALABILITY
        - EDITORIAL ANSWERS ARE GOOD
        """
        # make a copy of the board
        # board_copy = deepcopy(board)
        board_copy = []
        for row in board:
            row_copy = [val for val in row]
            board_copy.append(row_copy)

        ROWS = len(board)
        COLS = len(board[0])
        neighbors = [
            (1, 0), (-1, 0),  # horizontal
            (0, 1), (0, -1),  # vertical
            (1, 1), (-1, -1),  # positive digonal
            (-1, 1), (1, -1)  # negative diagonal
        ]

        # return 0 if cell is out of bounds or if cell is 0 ; 1 otherwise
        # rtype: int
        # parameter: row, col
        def getNeighborValue(row, col):
            if (
                0 <= row < ROWS and
                0 <= col < COLS and
                board_copy[row][col] == 1
            ):
                return 1
            return 0

        def nextStateOfCell(row, col):
            neighbor_total = sum(getNeighborValue(
                row + neigh_row, col + neigh_col) for neigh_row, neigh_col in neighbors)

            if board_copy[row][col] == 0:
                if neighbor_total == 3:
                    return 1
            else:
                if neighbor_total in {2, 3}:
                    return 1

            return 0

        # iterator over board_copy, change values of original board along the way
        for row in range(ROWS):
            for col in range(COLS):
                next_state = nextStateOfCell(row, col)
                board[row][col] = next_state
