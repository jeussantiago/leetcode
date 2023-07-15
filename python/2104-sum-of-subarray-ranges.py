class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        '''
        Brute Force
        - find every possible subarray
        - brute force in this situation of (n^2) is fine because constraints say that nums arr
        is max 1000 is length

        Time: O(n^2)
        Space: O(1)
        '''
        res = 0
        for left in range(len(nums)):
            min_val, max_val = nums[left], nums[left]
            for right in range(left + 1, len(nums)):
                min_val = min(min_val, nums[right])
                max_val = max(max_val, nums[right])

                res += (max_val - min_val)

        return res


'''
(n) Monotonic Stack
'''
