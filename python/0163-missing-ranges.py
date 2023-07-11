class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        '''

        Time: O(n)
        Space: O(n)

        '''
        res = []
        if not nums or nums[-1] != upper:
            nums.append(upper+1)

        if nums[0] != lower-1:
            nums = [lower-1] + nums

        low = lower
        for i, num in enumerate(nums):
            if num-1 >= lower and not (num-1 == nums[i-1]):
                res.append([low, num-1])

            low = num + 1

        return res
