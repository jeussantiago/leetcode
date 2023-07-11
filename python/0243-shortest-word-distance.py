class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        '''
        - just ypdate the position of index of word 1 and 2 continuously
        - if they have an index value, calculate the distance
        - this way, if a word appears multiple times, itll be updated

        Time: O(n)
        Space: O(1)
        '''

        res = len(wordsDict)-1
        i1, i2 = -1, -1
        for j, word in enumerate(wordsDict):
            if word == word1:
                i1 = j
            elif word == word2:
                i2 = j

            if i1 != -1 and i2 != -1:
                res = min(res, abs(i1 - i2))
        return res
