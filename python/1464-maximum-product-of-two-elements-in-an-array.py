class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        Time: O(n)
        Space: O(1)
        '''
        first, second = float('-inf'), float('-inf')
        for num in nums:
            if not first or num >= first:
                second = first
                first = num
            elif not second or num > second:
                second = num

        return (first - 1) * (second - 1)
