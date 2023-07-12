class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        '''
        don't need to iterate through entire battleship,
        can take advantage of the idea that the start of a battleship has:
            - as empty space it its left and
            - an empty space above it
        - this makes sure that you don't count theattached segments to the rest of the ship

        - this method saves space since you don't need to check the battlehsips positions every time

        Time: O(m * n)
        Space: O(1) 
        '''
        m, n = len(board), len(board[0])
        battleships = 0
        for row in range(m):
            for col in range(n):
                if (
                    board[row][col] == "X" and
                    (row == 0 or board[row-1][col] == ".") and
                    (col == 0 or board[row][col-1] == '.')
                ):
                    battleships += 1

        return battleships

        '''

        (although the constrictions say that no 2 battleships are adjacent, logic should still apply)
        | X X X     |
        | X         |
        |           |

        - if you check, the horizontal, keep checking horizontal until no more X end of board
        - else; check the vertical, same logic
        ["X",".",".","X"],
        [".",".",".","X"],
        [".",".",".","X"],
        ["X","X","X","."]

        Time: O(m * n) ; traverse entire board
        Space: O(m * n) ; board could be filled entirely with battleships with 1 space seperation
        '''

        # m, n = len(board), len(board[0])
        # battleships = 0
        # battleship_positions = set()
        # for row in range(m):
        #     for col in range(n):
        #         if (row, col) in battleship_positions or board[row][col] == ".":
        #             continue

        #         # position is an unvisited battleship
        #         battleships += 1
        #         battleship_positions.add((row, col))
        #         if col + 1 < n and board[row][col + 1] == 'X':
        #             c = col
        #             while c + 1 < n and board[row][c + 1] == 'X':
        #                 c += 1
        #                 battleship_positions.add((row, c))

        #         elif row + 1 < m and board[row + 1][col] == 'X':
        #             r = row
        #             while r + 1 < m and board[r + 1][col] == 'X':
        #                 r += 1
        #                 battleship_positions.add((r, col))

        # return battleships
