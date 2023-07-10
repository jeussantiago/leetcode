class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        - work outside in (border first to inside)
        - depth first search (dfs)

        iterating through board:
        - use len(board) then have a counter to tell us which row and col to search
            - if coutner = 1 then we would search len(board) - counter and 0 + counter 
            for the last row/col and the first row/col
        - do this until the left side >= right side (where left side is the first half and the right side
        is second half of board)

        check if a O should be flipped:
        - if its an "O"
            - check the adjacency
            - if its a top -> check bottom first
            - if its right -> check left first
            - if its bottom -> check top first
            - if its left -> check right first
        - 

        - go through border
        - dfs way through other connecting "O"
        - if current position is "x" or position is out of bounds; end recursion loop
        - if current position is "O" (still in bounds)
            - keep track of position in a set
            - if the position is already in the set, ignore that loop/recursion and just return
            - call function on adjacency positions

        - do dfs on border
        - then go through rest of board
            - if the position is not on the board or is not in the "O" set, set the "O" to a "X"


        [
            ["X","X","O","O","X"]
            ["X","O","O","O","X"]
            ["X","X","O","X","X"]
            ["X","O","X","O","X"]
            ["O","O","X","X","X"]
        ]

        [(0, 3), (0, 2), (1, 2), (1, 1), (1, 3), (2, 2), (3, 1), (4, 0), (4, 1)]


        Time: O(m * n)
        Space: O(m * n)
        """

        topRow, botRow, leftCol, rightCol = 0, len(board)-1, 0, len(board[0])-1
        visited_O_pos = set()

        def helper(row, col):
            if (
                not 0 <= row <= len(board)-1 or
                not 0 <= col <= len(board[0])-1 or
                board[row][col] == "X" or
                (row, col) in visited_O_pos
            ):
                return

            # current position is "O" and in bounds
            visited_O_pos.add((row, col))

            # go through adjacency positions
            # above
            helper(row-1, col)
            # to the right
            helper(row, col+1)
            # below
            helper(row+1, col)
            # to the left
            helper(row, col-1)

        # go through border and find connecting "O"s
        # top and bot
        for col in range(leftCol, rightCol + 1):
            helper(topRow, col)
            helper(botRow, col)

        # right and left sides
        for row in range(topRow, botRow + 1):
            helper(row, rightCol)
            helper(row, leftCol)

        # go through rest of board and change "O"s to "X"s
        for row in range(1, botRow):
            for col in range(1, rightCol):
                if (
                    board[row][col] == "O" and
                    (row, col) not in visited_O_pos
                ):
                    board[row][col] = "X"
