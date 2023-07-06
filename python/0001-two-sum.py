class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Time: O(n)
        Space: O(n)
        '''
        seenNums = {}
        for ind, num in enumerate(nums):
            remainingNum = target - num
            if remainingNum in seenNums:
                return [ind, seenNums[remainingNum]]
            
            seenNums[num] = ind