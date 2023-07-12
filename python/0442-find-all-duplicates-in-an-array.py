class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        '''
        - since all the values in the nums array are positive, and they appear either once or twice
        - we can just turn the number's index position into a negative the first time around, then check the second time
        around if its negative
        - if its negative, then this number is part of the results and appears twice

        Time: O(n)
        Space: O(1)
        '''
        res = []
        i = 0
        while i < len(nums):
            num = abs(nums[i])
            if nums[num - 1] < 0:
                # negative - num appeared second time
                res.append(num)
            else:
                # positive - num appeared for the first time
                nums[num - 1] *= -1
            i += 1

        return res
