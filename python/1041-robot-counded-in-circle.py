class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        '''
        Time: O(n)
        Space: O(1)
        '''
        # N, E, S, W
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        pos = [0, 0]
        i = 0

        for symbol in instructions:
            if symbol == 'R':
                i = (i + 1) % 4
            elif symbol == "L":
                i = (i - 1) % 4
            else:
                pos[0] += directions[i][0]
                pos[1] += directions[i][1]

        # robot back to center or doesnt face north
        return pos == [0, 0] or i != 0
