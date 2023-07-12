class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        '''
        Time: O(n^2)
        Space: O(n)
        '''

        MOD = 10 ** 9 + 7

        def dfs(nums):
            n = len(nums)
            if n < 3:
                return 1

            root = nums[0]
            left = [num for num in nums if num < root]
            right = [num for num in nums if num > root]
            n, k = n - 1, len(left)
            return (
                math.comb(n, k) * dfs(left) * dfs(right)
            ) % MOD

        return (dfs(nums) - 1) % MOD
