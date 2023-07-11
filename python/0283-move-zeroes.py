class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        2 pointers
        if right pointer == 0:
            right += 1
        if right pointer != 0:
            - swap left and right pointers
            left += 1
            right += 1

        [1,3,0,0,12]

        Time: O(n)
        Space: O(1)
        """

        zero_ptr = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero_ptr], nums[i] = nums[i], nums[zero_ptr]
                zero_ptr += 1
