class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        '''
        S is the length of strs
        Time: O(S * m * n)
        Space: O(S * m * n)
        '''

        weights = [Counter(s) for s in strs]
        cache = {}

        def dfs(ind, m, n):
            if m < 0 or n < 0 or ind >= len(strs):
                return 0

            if (ind, m, n) in cache:
                return cache[(ind, m, n)]

            # skip
            res = dfs(ind + 1, m, n)

            # factor current string
            if m - weights[ind]['0'] >= 0 and n - weights[ind]['1'] >= 0:
                res = max(
                    res, dfs(ind + 1, m - weights[ind]['0'], n - weights[ind]['1']) + 1)

            cache[(ind, m, n)] = res
            return cache[(ind, m, n)]

        return dfs(0, m, n)
