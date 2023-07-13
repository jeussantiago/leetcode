class Solution:
    def judgeCircle(self, moves: str) -> bool:
        '''
        Time: O(n)
        Sapce: O(1)
            ; although we use a dictionary, the size of the dictionary is at most 4
        '''
        pos = collections.defaultdict(int)
        for move in moves:
            pos[move] += 1
        return pos['U'] == pos['D'] and pos['R'] == pos['L']


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        '''
        Time: O(n)
        Space: O(1)
        '''

        pos = [0, 0]
        for move in moves:
            if move == 'U':
                pos[1] += 1
            elif move == 'D':
                pos[1] -= 1
            elif move == 'R':
                pos[0] += 1
            else:
                pos[0] -= 1

        return pos == [0, 0]
