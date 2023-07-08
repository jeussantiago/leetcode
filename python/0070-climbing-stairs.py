class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        n = 1 : steps = 1
        n = 2 : steps = 2
        n = 3 : steps = 3
        n = 4 : steps = 5
        n = 5 : steps = 8
        n = 6 : steps = 13
        n = 6
        [0,0,0,0,0,0,0] ; n+1
        [1,2,0,0,0,0,0]
        pos i (3) = pos i-1 (2) + pos i-2 (1)
        pos i (3) = 3
        [1,2,3,0,0,0,0]

        - this problem pretty much is fibonacci sequence

        Time: O(n)
        Space: O(n)
        '''
        if n <= 2: return n
        dp = [0] * (n)
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]