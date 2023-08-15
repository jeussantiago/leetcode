class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        '''
        BFS:

        - roll the ball in the 4 directions

        - wherever the ball stops, 
            if stop_pos 2:
                    - don't add to queue
            else if stop_pos == 0
                we modify the maze by saving a "2" in the position

        [
            [0,0,1,2,2],
            [0,0,0,0,0],
            [0,0,0,1,2],
            [1,1,0,1,1],
            [0,0,0,0,0]
        ]
        queue = [(0,3)]
        - we don't add (0,4) back into the array because it was already 2

        [
            [2,2,1,2,2],
            [2,0,2,2,2],
            [2,2,2,1,2],
            [1,1,0,1,1],
            [2,0,2,0,2]
        ]

        - at the end, we just need to check if the deestination is a 2

        m * n is size of maze
        Time: O(m * n)
        Space: O(1)
            ; not using extra space, modifying the given input maze
        '''
        ROWS, COLS = len(maze), len(maze[0])
        maze[start[0]][start[1]] = 2
        q = collections.deque([start])

        while q:
            row, col = q.pop()
            if [row, col] == destination:
                return True

            tmp_row = row
            # check up
            while tmp_row - 1 >= 0 and maze[tmp_row-1][col] != 1:
                tmp_row -= 1
            if maze[tmp_row][col] != 2:
                maze[tmp_row][col] = 2
                q.appendleft([tmp_row, col])
            # check down
            tmp_row = row
            while tmp_row + 1 < ROWS and maze[tmp_row + 1][col] != 1:
                tmp_row += 1
            if maze[tmp_row][col] != 2:
                maze[tmp_row][col] = 2
                q.appendleft([tmp_row, col])

            # check right
            tmp_col = col
            while tmp_col + 1 < COLS and maze[row][tmp_col + 1] != 1:
                tmp_col += 1
            if maze[row][tmp_col] != 2:
                maze[row][tmp_col] = 2
                q.appendleft([row, tmp_col])

            # check left
            tmp_col = col
            while tmp_col - 1 >= 0 and maze[row][tmp_col - 1] != 1:
                tmp_col -= 1
            if maze[row][tmp_col] != 2:
                maze[row][tmp_col] = 2
                q.appendleft([row, tmp_col])

        return False
