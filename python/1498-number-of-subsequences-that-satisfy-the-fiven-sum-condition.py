class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        '''
        - sorting the input brings the same results but just in a different order
        Time: O(nlogn)
        Space: O(1)
        '''
        mod = 10 ** 9 + 7
        nums.sort()
        res = 0
        for left, left_num in enumerate(nums):
            right = bisect_right(nums, target - left_num) - 1
            if right >= left:
                res += pow(2, right - left, mod)

        return res % mod
