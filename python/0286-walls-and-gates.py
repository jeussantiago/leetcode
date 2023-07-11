class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        gates = [(0,2), (3,0)]

        {
            (0,0): [(1,0)]
            (3,0): [(0,2)]
            (1,0): [(0,0), (1,1), (2,0)]
            (1,1): [(1,2), (1,0)]
            (1,2): [(0,2), (1,1), (2,2)]
        }

        Previous Thought:
        - get the positions of the gates
        - do dfs to calculate the the distance between a square and the gate
        Time: O((mn)^2)

        => we can reduce the time complexity if we search at the same time (BFS)

        - add the gate positions to the queue
        - go to the neighboring positions if it is not a gate or a wall
            - in that position, replace the value with the current steps
            - go to its neighbors,
                - if its in bounds, not a gate or a wall, and not in visited
                    - add the neighbor to the queue
                    - add current position to visited positions

        Time: O(mn)
        Space: O(mn)
        """
        M, N = len(rooms), len(rooms[0])
        visited = set()
        q = collections.deque()

        # get the gates/ fill the queue
        for i, row in enumerate(rooms):
            for j, room in enumerate(row):
                if room == 0:
                    q.appendleft((i, j))
                    visited.add((i, j))

        # traverse to a room if it is in bounds, not have been visted before, and not a wall
        def addRoom(row, col):
            if (
                0 <= row < M and
                0 <= col < N and
                (row, col) not in visited and
                rooms[row][col] != -1
            ):
                q.appendleft((row, col))
                visited.add((row, col))

        # go to room neighbors and fill the room size
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        steps = 0
        while q:
            for _ in range(len(q)):
                row, col = q.pop()
                rooms[row][col] = steps

                # go to neighbors of current room
                for i, j in neighbors:
                    addRoom(row + i, col + j)

            steps += 1

        for room in rooms:
            print(room)
