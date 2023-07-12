class Solution:
    def maxA(self, n: int) -> int:
        '''
        - paste "A" -> 1 press
        - paste whatever was copied before -> 1 press
        - or select all, copy, then paste -> 3 presses

        T: O(n)
        S: O(n)
        '''
        dp = list(range(n + 1))
        for i in range(7, n+1):
            dp[i] = max(
                2 * dp[i - 3],
                3 * dp[i - 4],
                4 * dp[i - 5]
            )
        return dp[n]
