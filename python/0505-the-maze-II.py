class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        '''
        minHeap / BFS

        - store the (distance, curr_row, curr_col) in the minHeap
        - have a cache with key=(curr_row, curr_col) value=(distance)
            - we only add to the minHeap and update cache if the value in the cache doesn't exist or
            if the value in the cache is > the curr_distance
            - if the value in the cache is <= then we don't need to keep going with the search for this
            instance

        - if the (curr_row, curr_col) == destination then we can stop searching and return this distance
        - if the minHeap is empty then we can also stop searching and return -1 since we never 
        reached destination

        n is the length of maze rows
        m is the length of max columns
        k is the number of possible distances
        Time: O(n * m * k)
            ; need to keep searching if the distance on the same row,col is the less than
        Space: O(n * m)
            ; cache
        '''
        ROWS, COLS = len(maze), len(maze[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def getNextBallPos(row, col, dy, dx):
            steps = 0
            while (
                0 <= row + (dy * (steps + 1)) < ROWS and
                0 <= col + (dx * (steps + 1)) < COLS and
                maze[row + (dy * (steps + 1))][col + (dx * (steps + 1))] == 0
            ):
                steps += 1

            new_row, new_col = row + (dy * (steps)), col + (dx * (steps))
            return (new_row, new_col), max(abs(new_row - row), abs(new_col - col))

        minHeap = [(0, start[0], start[1])]
        cache = {(start[0], start[1]): 0}
        while minHeap:
            distance, row, col = heappop(minHeap)

            if [row, col] == destination:
                return distance

            for dy, dx in directions:
                next_pos, distance_diff = getNextBallPos(row, col, dy, dx)
                total_dist = distance + distance_diff
                if next_pos not in cache or total_dist < cache[next_pos]:
                    cache[next_pos] = total_dist
                    heappush(minHeap, (total_dist, next_pos[0], next_pos[1]))

        return -1
