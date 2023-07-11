class Solution:
    def integerBreak(self, n: int) -> int:
        '''
        n  = [1,2,3,4]
        dp = [1,2,_,_]

        - go up to current_n
        for i in range(1, 3)
            - calculate all the possiblilities of the sub problems
            - (1,2)
            - (2,1)
            (calculate the product of the 2)

        - if current_n != n
            - we can initally set the dp[current_n] to be current_n
        - if current_n == n
            - set it to 0

        - only iterate through the first half, iterating through the second half is the same as iterating over first half

        Time: O(n^2)
        Space: O(n)
        '''
        dp = [num for num in range(n+1)]
        dp[-1] = 0

        for num in range(2, n+1):
            for i in range(1, math.floor(num // 2) + 1):
                val = dp[i] * dp[num - i]
                dp[num] = max(dp[num], val)

        return dp[-1]
