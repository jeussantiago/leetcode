class Solution:
    def hIndex(self, citations: List[int]) -> int:
        '''
        [0,1,3,5,6]
        if mid == N - mid
            retrurn N - mid

        if mid < N - mid:
            l = mid + 1
        else;
            r = mid -1

        Time: O(logn)
        Space: O(1)
        '''
        N = len(citations)
        l, r = 0, N - 1

        while l <= r:
            mid = (l + r) // 2

            if citations[mid] == N - mid:
                return N - mid

            if citations[mid] < N - mid:
                l = mid + 1
            else:
                r = mid - 1

        # no exact match, return the index position where there are h papers that have atleast h citaitons
        return N - l
