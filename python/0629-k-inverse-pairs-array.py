class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        '''
        Time: O(n * k)
        Space: O(n * k)
        '''
        MOD = 10 ** 9 + 7
        cache = {}

        def dfs(n, k):
            # if no more pairs, stop, valid output
            if k == 0:
                return 1
            # no more numbers and no more pairs available
            if n <= 0 or k < 0:
                return 0

            if (n, k) in cache:
                return cache[(n, k)]

            cache[(n, k)] = (
                # skip the current number -> assumes that it doesn't create an inverse pair
                dfs(n - 1, k)
                # accept current number -> assumes that it creates an inverse pair
                + dfs(n, k - 1)
                # Adjusting for cases where the current number creates multiple inverse pairs.
                - dfs(n - 1, k - n)
            ) % MOD

            return cache[(n, k)]

        return dfs(n, k)
