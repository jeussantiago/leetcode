class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        '''
        Time: O(n)
        Space: O(n)
        '''
        MOD = 10 ** 9 + 7

        cache = {}

        def dfs(length):
            if length > high:
                return 0

            if length in cache:
                return cache[length]

            cache[length] = 1 if length >= low else 0
            # add number of zero to string '000'
            # add number of ones to string '11'
            cache[length] += dfs(length + zero) + dfs(length + one)
            cache[length] = cache[length] % MOD
            return cache[length]

        return dfs(0)
