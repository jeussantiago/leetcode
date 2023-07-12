class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        '''
        Time: O(n)
            ; because of caching, we only visit each position once, with 3 loops which would be (1)
        Space: O(n)
            ; size of cache would be size of given array
        '''
        cache = {}

        def dfs(ind):
            if ind == len(stoneValue):
                return 0

            if ind in cache:
                return cache[ind]

            res = float('-inf')
            total = 0
            for j in range(ind, min(ind + 3, len(stoneValue))):
                total += stoneValue[j]
                res = max(res, total - dfs(j + 1))

            cache[ind] = res
            return res

        winner = dfs(0)

        if winner > 0:
            return "Alice"
        elif winner < 0:
            return "Bob"
        else:
            return "Tie"
