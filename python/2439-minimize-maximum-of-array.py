class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        '''
        Time: O(n)
        Sapce: O(1)
        '''
        total = 0
        res = 0
        for i, num in enumerate(nums):
            total += num
            avg = math.ceil(total / (i+1))
            res = max(res, avg)

        return res
