class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        '''
        Dijkstra's Algorithm

        minHeap
            - keep a record of the distance traveled
            - string instructions
            - current row, col position

        - at each point, we will take the minimum distance in the heap and roll the ball in the four directions
        - if the ball ends up in a location that was already visited, then that means that in a different path, the ball was able to reach that location in a shorter number of steps which means we don't add that new location


        - even if we land in the hole, we need to know the lexographical order
            - however, if we put the string in the second position in the minHeap, it will automatically order
            so we can just return the answer
        - even if we reach the hole, we put it back into the minHeap, so that it sorts itself

        - we keep doing this until the minHeap is empty or we find a solution

        mn is the size of the maze
        Time: O(mnlog(mn))
            ; (m*n) visit each position one time
            ; (mnlog(mn)) adding to the heap
            ; (mnlog(mn)) popping from the heap 
        Space: O(m*n)
            ; (m*n) minHeap
            ; (m*n) visited set
        '''
        ROWS, COLS = len(maze), len(maze[0])
        directions = [(0, -1, 'l'), (-1, 0, 'u'), (0, 1, 'r'), (1, 0, 'd')]
        minHeap = [(0, "", ball[0], ball[1])]
        visited = set()

        def valid(row, col):
            return 0 <= row < ROWS and 0 <= col < COLS and maze[row][col] == 0

        def getNeighbors(row, col):
            neighbors = []
            for dy, dx, next_instruct in directions:
                curr_row, curr_col = row, col
                dist = 0
                # move the ball to the next position and check if valid
                while valid(curr_row + dy, curr_col + dx):
                    curr_row += dy
                    curr_col += dx
                    dist += 1
                    if [curr_row, curr_col] == hole:
                        break

                neighbors.append((dist, next_instruct, curr_row, curr_col))

            return neighbors

        while minHeap:
            curr_dist, instructions, row, col = heappop(minHeap)

            if (row, col) in visited:
                continue

            if [row, col] == hole:
                return instructions

            visited.add((row, col))

            # get the neighbors
            neighbors = getNeighbors(row, col)
            for dist, next_instruct, next_row, next_col in neighbors:
                heappush(minHeap, (curr_dist + dist, instructions +
                         next_instruct, next_row, next_col))

        return "impossible"
