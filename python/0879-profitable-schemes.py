class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        '''
        Bottom Up DP:

        '''
        MOD = 10**9 + 7
        dp = []
        for _ in range(len(group) + 1):
            dp.append([[0] * (minProfit + 1) for _ in range(n + 1)])

        # base case
        for m in range(n + 1):
            dp[len(group)][m][minProfit] = 1

        for i in range(len(group) - 1, -1, -1):
            for m in range(n + 1):
                for p in range(minProfit + 1):
                    dp[i][m][p] = dp[i+1][m][p]
                    if m + group[i] <= n:
                        dp[i][m][p] += dp[i+1][m + group[i]
                                               ][min(minProfit, p + profit[i])] % MOD

        return dp[0][0][0] % MOD


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        '''
        Top Down Recursion:

        n = 10, minProfit = 5, group = [2,6,5,4], profit = [6,7,2,4]
        res = [(0),(0,1),(0,2),(0,3)
               (1),(1,3)
               (2,3)]
        dfs(i, remaning_n, profit)

        - we current profit might get really big, we don't care how big it gets, just the fact that it's over the minProfit
            - too help with runtime, we want to cache that by only saving the the profit if it hasn't reached the minProfit yet
            or the minProfit if it is smaller


        N is the number of criminals allowed in a crime
        M is the size of list group
        K is the value of minProfit. this is important because we can top iterating over values greater than minProfit by 
        storing the min of current profit and the minProfit
        Time: O(N * M * K)
        Space: O(N * M * K); the max recursion calls is N 
        '''
        MOD = 10**9 + 7
        cache = {}

        def dfs(i, remaining_n, curr_profit):
            if i >= len(group):
                return 1 if curr_profit >= minProfit else 0

            if (i, remaining_n, curr_profit) in cache:
                return cache[(i, remaining_n, curr_profit)]

            # skip current crime
            cache[(i, remaining_n, curr_profit)] = dfs(
                i + 1,  remaining_n, curr_profit)

            # go to a crime if there are enough group space
            if remaining_n - group[i] >= 0:
                cache[(i, remaining_n, curr_profit)] += dfs(i + 1, remaining_n -
                                                            group[i], min(minProfit, curr_profit + profit[i]))

            return cache[(i, remaining_n, curr_profit)] % MOD

        return dfs(0, n, 0)
