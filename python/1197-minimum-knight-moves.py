class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        '''
        BFS:

        - keep a record of the 8 possible directions a knight can move
        - if the positiion is visited then don't add
        - otherwise, add the position to the queue

        n is the number of moves
        Time: O(8^n)
            ; 8 possible decisions at each point
            ; height of tree/number of moves is n
        Space: O(n)
            ; (n) max amount of space the knight will move, according to the
            ; constrainst is 300 but we'll just say n
        '''
        directions = [(1, 2), (2, 1), (2, -1), (1, -2),
                      (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        q = collections.deque([(0, 0)])
        visited = set()
        steps = 0
        while q:
            for _ in range(len(q)):
                curr_y, curr_x = q.pop()

                if (curr_y, curr_x) == (y, x):
                    return steps

                for dy, dx in directions:
                    next_y, next_x = curr_y + dy, curr_x + dx
                    if (next_y, next_x) not in visited:
                        visited.add((next_y, next_x))
                        q.appendleft((next_y, next_x))

            steps += 1
