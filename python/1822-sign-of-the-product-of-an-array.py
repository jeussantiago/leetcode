class Solution:
    def arraySign(self, nums: List[int]) -> int:
        '''
        Time: O(n)
        Space: O(1)

        '''
        sign = 1
        for num in nums:
            if num == 0:
                return 0
            sign *= num

        return 1 if sign > 0 else -1
