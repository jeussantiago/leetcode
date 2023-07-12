class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        '''
        [1,2,3,4,5,6]

        [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]  of length 3, n = 4
        [1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]    of length 4, n = 3
        [1, 2, 3, 4, 5], [2, 3, 4, 5, 6]            of length 5, n = 2
        [1, 2, 3, 4, 5, 6]                          of length 6, n = 1

        Time: O(n)
        Space: O(n)
        '''
        N = len(nums)
        if N < 3:
            return 0

        dp = [0] * N
        for i in range(2, N):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp[i] = dp[i-1] + 1

        return sum(dp)
