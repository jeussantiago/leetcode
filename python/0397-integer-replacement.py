class Solution:
    def integerReplacement(self, n: int) -> int:
        cache = {}

        def dfs(num):
            if num == 1:
                return 0
            if num in cache:
                return cache[num]

            if num % 2:
                # odd
                cache[num] = min(dfs(num-1), dfs(num+1)) + 1
            else:
                # even
                cache[num] = dfs(num//2) + 1

            return cache[num]

        return dfs(n)
