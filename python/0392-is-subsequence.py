class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
        2 pointer

        S is length of s
        T is length of t
        Time: O(S + T)
        Space: O(1)
        '''
        S, T = len(s), len(t)
        i, j = 0, 0

        while i < S and j < T:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1

        return i == S
