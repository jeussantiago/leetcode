class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        '''
        Time: O(n)
        Space: O(n)
        '''
        pos = {}
        for ind, c in enumerate(keyboard):
            pos[c] = ind

        res = 0
        prev_ind = 0
        for c in word:
            res += abs(pos[c] - prev_ind)
            prev_ind = pos[c]

        return res
