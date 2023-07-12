class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        '''
        Bottom Up DFS
        - kinda have to brute force it since you need to visit every position since it wants subsequence

        - can reduce time with memoization

        Time: O(n^2)
        Space: O(n^2)
        '''

        cache = {}

        def dfs(l, r):
            if (l, r) in cache:
                return cache[(l, r)]

            if l == r:
                # same char
                return 1

            if l > r:
                return 0

            if s[l] == s[r]:
                cache[(l, r)] = dfs(l+1, r-1) + 2
            else:
                cache[(l, r)] = max(dfs(l+1, r), dfs(l, r-1))

            return cache[(l, r)]

        return dfs(0, len(s) - 1)
