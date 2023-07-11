class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        '''
        - sorting, first num increasing, second number decrasing
        [[2, 100], [3, 200], [4, 300], [5, 500], [5, 400], [5, 250], [6, 370], [6, 360], [7, 380]]

        - Longest Increasing Subsequence (LIS) - #300

        one at a time, we insert the second number into the dp array: arr will initially be emptied
        - binary search to see where we can place the second num
        - the concept is that we just replace numbers if this number is less than the number, 
            - since we want less than, we use bisect_left
            - the deccrementing of the second num is important since we want to see the smaller envelopes later if
            the current size is the same (same width, decreasing height)

        [100, 200, 300, 500]
        [100, 200, 250, 400]
        [100, 200, 250, 370]
        [100, 200, 250, 360]
        [100, 200, 250, 360, 380]


        Time: O(nlogn + nlogn) sorting + getting solution
            : O(nlogn)
        Space: O(n) python sorting
        '''
        envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))

        dp = []
        for _, height in envelopes:
            ind = bisect_left(dp, height)
            if ind == len(dp):
                dp.append(height)
            else:
                dp[ind] = height

        return len(dp)
