class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        '''
        - there are some spaces we don't visit
        - we only need to focus on the positions of the robots
        - we need to keep track of the current values while the robots remain on the same row
            - col values can be different

        - find all the combinations of the current_row, for left_robot_col_pos with right_robot_col_pos
        [left_robot_col_1, left_robot_col_2, left_robot_col_3] * [right_robot_col_1, right_robot_col_2, right_robot_col_3]

        M is the numebr of rows
        N is the number of cols
        Time: O(M * N^2)
            ; (M * N * N) row * robot_1_col * robot_2_col
        Space: O(M * N^2)
            ; (M) recursion stack
            ; (M * N * N) cache
        '''

        ROWS, COLS = len(grid), len(grid[0])

        @cache
        def dfs(row, left_robot_col, right_robot_col):
            # ignore out of bounds positions
            if (
                row >= ROWS
                or left_robot_col < 0
                or left_robot_col >= COLS
                or right_robot_col < 0
                or right_robot_col >= COLS
            ):
                return 0

            # add the cherries from the left robot
            cherries = grid[row][left_robot_col]
            # only add the cherries from the right robot its not in the same grid position
            if left_robot_col != right_robot_col:
                cherries += grid[row][right_robot_col]

            # go through all the possible next positions for the robots
            temp = 0
            for next_left_robot_col in [-1, 0, 1]:
                for next_right_robot_col in [-1, 0, 1]:
                    temp = max(temp, dfs(row + 1, left_robot_col +
                               next_left_robot_col, right_robot_col + next_right_robot_col))

            cherries += temp
            return cherries

        return dfs(0, 0, COLS - 1)
