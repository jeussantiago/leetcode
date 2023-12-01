class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        '''
        Time: O(n + m)
        Space: O(1)
        '''
        return "".join(word1) == "".join(word2)
