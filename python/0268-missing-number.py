class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        curr_num = 0  # what the current number should be
        for num in nums:
            if num != curr_num:
                return curr_num
            curr_num += 1
        return curr_num
