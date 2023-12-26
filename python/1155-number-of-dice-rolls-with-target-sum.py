class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        '''
        t is the number range up to  target
        Time: O(n * t * k)
        Space: O(n * t)
        '''

        MOD = 10 ** 9 + 7
        cache = collections.defaultdict(int)

        def dfs(n, target):
            if n == 0:
                return 1 if target == 0 else 0

            if (n, target) in cache:
                return cache[(n, target)]

            total = 0
            for dice_roll in range(1, k + 1):
                total = (total + dfs(n - 1, target - dice_roll)) % MOD

            cache[(n, target)] = total
            return total

        return dfs(n, target)
