class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        - can't be greedy
        coins = [1,3,4,5] ; amount = 7
        - greedy would say [5,1,1] is the answer but the actual answer is [4,3]  

        dp[0] = 0
        dp[1] = 1
        dp[2] = 1 + dp[1]
        dp[3] = 1
        dp[4] = 1
        dp[5] = 1
        dp[6] = 2
        - if we use the 1 coin
        dp[7] = 1 + dp[i-1] = 1 + dp[6] = 1 + 2
        - we can also use the next coin
        dp[7] = 1 + dp[i-3] = 1 + dp[4] = 1 + 1
        dp[7] = 1 + dp[i-4] = 1 + dp[3] = 1 + 1
        dp[7] = 1 + dp[i-5] = 1 + dp[2] = 2 + 1
        dp[7] = min(all coins)


        Time: O(n * S) ; where n is the len of coins and S is the amount 
        Space: O(S) ; 
        '''
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for amnt in range(1, (amount + 1)):
            for coin in coins:
                if amnt - coin >= 0:
                    dp[amnt] = min(dp[amnt], 1 + dp[amnt - coin])

        return dp[amount] if dp[amount] != float("inf") else -1
