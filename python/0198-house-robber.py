class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
            2 7 9  3  1 
            2 7 11 11 12

            2 1 1 5 1
            2 2 3 7 7

            - max(i-2 + i, i-1)

        Time: O(n)
        Space: O(n) (can make it O(1) if you just saved the last two variables instead of an array)
        '''

        N = len(nums)
        if N == 1:
            return nums[0]

        dp = [0] * N
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, N):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        return dp[-1]
