class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        '''
        Time: O(nlogn)
        Space: O(n)
            ; sorting space
        '''
        nums.sort()
        N = len(nums)
        res = 0
        for i in range(N // 2):
            res = max(res, nums[i] + nums[N - i - 1])

        return res
