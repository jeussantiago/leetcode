class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        Recursion (top-down):
        t1 is the length of text1
        t2 is the length of text2
        Time: O(t1 * t2)
        Space: O(t1 * t2) ; recursion stack max(t1, t2)
        '''
        T1, T2 = len(text1), len(text2)
        cache = {}

        def dfs(i, j):
            if i >= T1 or j >= T2:
                return 0

            if (i, j) in cache:
                return cache[(i, j)]

            if text1[i] == text2[j]:
                cache[(i, j)] = dfs(i + 1, j + 1) + 1
            else:
                cache[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))

            return cache[(i, j)]

        return dfs(0, 0)


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        DP (top-down):
        t1 is the length of text1
        t2 is the length of text2
        Time: O(t1 * t2)
        Space: O(t1 * t2)
        '''
        T1, T2 = len(text1), len(text2)
        # +1 for base case of  0
        dp = [[0] * (T2 + 1) for _ in range(T1 + 1)]

        for i in range(1, T1 + 1):
            for j in range(1, T2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]
