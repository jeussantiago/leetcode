class Solution:
    def hIndex(self, citations: List[int]) -> int:
        '''
        [0,1,3,5,6,8,9]
        m = 3

        Time: O(nlogn)
        Space: O(1)
        '''
        N = len(citations)
        citations = sorted(citations)
        i = 0
        while i < N and citations[N - 1 - i] > i:
            i += 1
        return i
