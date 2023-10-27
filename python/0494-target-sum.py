class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        choice between '+' or '-'

        DFS
            - current index
            - current total

            - return value: the count of total == target

        n is the length of nums
        t is the possible sum of nums
        Time: O(n * t)
        Space: O(n * t)
        '''
        cache = collections.defaultdict(int)

        def dfs(ind, total):
            if ind == len(nums):
                return int(total == target)

            if (ind, total) in cache:
                return cache[(ind, total)]

            # num is positive
            cache[(ind, total)] = dfs(ind + 1, total + nums[ind])
            # nums is negative
            cache[(ind, total)] += dfs(ind + 1, total - nums[ind])

            return cache[(ind, total)]

        return dfs(0, 0)
