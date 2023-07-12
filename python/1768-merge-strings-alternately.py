class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        '''
        n is the len of word1 and m is the len of word2
        Time: O(n + m)
        Space: O(1)
        '''
        res = ""
        last_ind = min(len(word1), len(word2))
        for i in range(last_ind):
            res += word1[i] + word2[i]

        if last_ind < len(word1):
            res += word1[last_ind:]
        elif last_ind < len(word2):
            res += word2[last_ind:]

        return res
