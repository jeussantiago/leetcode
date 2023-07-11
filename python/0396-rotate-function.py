class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        '''
        Time: O(n)
        Space: O(n)
        '''

        n = len(nums)
        total = sum(nums)
        F = [0] * n
        for i, num in enumerate(nums):
            F[0] += (i * num)

        for i in range(1, n):
            F[i] = F[i-1] + total - n * nums[n-i]

        return max(F)
