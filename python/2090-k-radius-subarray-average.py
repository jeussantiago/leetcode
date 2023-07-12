class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        '''
        queue:
        - uses extera space

        two pointers:
        - saves space

        Time: O(n)
        Space: O(1)
        '''

        res = [-1] * len(nums)
        n = len(nums)

        if k == 0:
            return nums

        if (2 * k + 1) > n:
            return res

        l = 0
        total = sum(nums[:2 * k + 1])
        res[k] = total // (2 * k + 1)

        for i in range(2 * k + 1, n):
            total += nums[i] - nums[i - (2 * k + 1)]
            res[i - k] = total // (2 * k + 1)

        return res
