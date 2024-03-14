class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        '''
        Prefix Sum

        Time: O(n)
        Space: O(n)
        '''
        total, res = 0, 0
        freq = collections.defaultdict(int)
        for num in nums:
            total += num
            if total == goal:
                res += 1

            if total - goal in freq:
                res += freq[total - goal]

            freq[total] += 1

        return res


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        '''
        DFS - TLE

        Time: O(n^2)
        Space: O(n)
        '''
        N = len(nums)

        def dfs(start):
            if start >= N:
                return 0

            # skip current and start a new
            res = dfs(start + 1)
            # count the items to the count
            total = 0
            for ind in range(start, N):
                if total > goal:
                    break

                total += nums[ind]

                if total == goal:
                    res += 1

            return res

        return dfs(0)
