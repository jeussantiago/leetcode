
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        '''
        - check if direction is increasing
        - check if direction is decreasing

        Time: O(n)
        Space: O(1)
        '''

        inc = dec = True
        for i in range(len(nums) - 1):
            if nums[i + 1] < nums[i]:
                inc = False
            if nums[i + 1] > nums[i]:
                dec = False

        return inc or dec
