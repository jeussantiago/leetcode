class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        '''
        Sliding Window

        62 + 136 = 198

        Time: O(nlogn)
            ; (nlogn) sorting
            ; (n) traversing through array
        Space: O(1)
            ; (n) python sorting - not counting
        '''
        nums.sort()
        left, right = 0, len(nums) - 1
        res = -1
        while left < right:
            if nums[left] + nums[right] >= k:
                right -= 1
            else:
                res = max(res, nums[left] + nums[right])
                left += 1
        return res


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        '''
        Time: O(n^2)
        Space: O(1)
        '''
        res = -1
        for i, num1 in enumerate(nums):
            for j in range(i + 1, len(nums)):
                num2 = nums[j]
                if num1 + num2 < k:
                    res = max(res, num1 + num2)

        return res
