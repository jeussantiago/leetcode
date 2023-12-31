class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        '''
        Time: O(n)
        Space: O(1)
            ; (26) hashmap will contain only lowercase english letters
        '''
        last_appearance = {}
        res = -1
        for i, c in enumerate(s):
            if c not in last_appearance:
                # first appearance of char
                last_appearance[c] = i
            else:
                substring_len = i - last_appearance[c] - 1
                res = max(res, substring_len)

        return res
