class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        '''
        - keep a min-heap of the boundaries
        - values in heap are [height, boundary_i, boundary_j]

            - start with the outside edges of the matrix

            - constantly pop the min of the heap
            - if the min_val has neighbors that are unvisited
                - explore the boxes connected to this position

                - if the connection is lower:
                    - store the heigh difference/water volume in that connection position
                    - push the current number back onto the heap, we want to keep the max height thats why

                    [
                        [12,12,12,12,12,12]
                        [ 4, 2, 3, 4, 2, 4]
                        [12,12,12,12,12,12]
                    ]

                    - the 2 on the left,
                        - to calculate the water volume in that position, we want the difference between height=4 and current_height=2
                        not between height=3 and current_height=2


                - if the connection is higher:
                    - push the new connection height onto the heap

                (could also just throw the higher number out of the two back into the heap)

        - to show that something has been visited, we could:
            - have a visited set ()
            - or at each position just store a -1


        N is the row length
        M is the col length
        h is the height of the heap
        Time: O(M * N * logh)
                ; (2N + 2M) creating the inital heap - boundaries
                ; (h) heapify

                ; (M * N) calculating for every position
                    ; (logh) heap pop
                    ; (logh) push back into the heap
                ; (M * N * logh * logh)

        Space: O(h)
        '''
        N, M = len(heightMap), len(heightMap[0])
        minHeap = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # fill the heap with the initail boundaries
        for row in range(N):
            for col in range(M):
                if row in {0, N-1} or col in {0, M-1}:
                    minHeap.append((heightMap[row][col], row, col))
                    heightMap[row][col] = -1

        heapq.heapify(minHeap)

        res = 0
        while minHeap:
            height, row, col = heapq.heappop(minHeap)

            for dx, dy in directions:
                x, y = row + dx, col + dy

                # check if position is invalid or if neighbor has been visited already
                if (
                    x < 0 or x >= N or
                    y < 0 or y >= M or
                    heightMap[x][y] == -1
                ):
                    continue

                # lower connection
                if heightMap[x][y] < height:
                    # record the water volume added
                    res += (height - heightMap[x][y])
                    # keep the higher number, which is the boundary height, as the height when pushing the new boundary onto the heap
                    heapq.heappush(minHeap, (height, x, y))
                else:
                    # higher connection - no need to record difference in water
                    # store the higher number, which is the new connection, in the heapmap
                    heapq.heappush(minHeap, (heightMap[x][y], x, y))

                # show that position has been visited
                heightMap[x][y] = -1

        return res
