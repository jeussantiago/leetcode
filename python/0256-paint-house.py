class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        '''
        - at the current index, add the minimum total from the previous houses, not including itself
        - 18 = 16 + min(2, 17)
        [
            17 2  17
            18 33 7
            21 10 37
        ]

        Time: O(n * 3)
            : O(n)
        Space: O(3)
             : O(1)
        '''

        dp = costs[0]

        for i in range(1, len(costs)):
            house = costs[i]
            dp0 = house[0] + min(dp[1], dp[2])
            dp1 = house[1] + min(dp[0], dp[2])
            dp2 = house[2] + min(dp[0], dp[1])
            dp = [dp0, dp1, dp2]

        return min(dp)
