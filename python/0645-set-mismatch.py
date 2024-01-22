class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        '''
        No extra space used

        Time: O(n)
        Space: O(1)
        '''
        # find the repeating number
        repeating_num = None
        for i, num in enumerate(nums):
            num = abs(num)
            if nums[num - 1] < 0:
                # current number is the repeating number
                repeating_num = num
            else:
                nums[num - 1] *= -1

        # find the missing number
        missing_num = None
        for i, num in enumerate(nums):
            if num > 0:
                # number hasn't been changed to negative to signify that the number appears
                missing_num = i + 1
                break

        return [repeating_num, missing_num]
