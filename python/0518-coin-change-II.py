class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        '''
        DP (Space Optimizaion)

        - similar with the DP solution (no space optimization)
        - we notice that we need to know the entirety of the amount array for the current coin
        - however, we don't need to remember all of the coin's amounts, we only need to remember the coin that
        is directly beneath
        - so we only to remember 2 arrays of length amount

                    amount                                  amount
                    5 4 3 2 1 0                             5 4 3 2 1 0
         coins  2  [1,1,0,1,0,1]       =>               1  [4,3,2,2,1,1] 
                5  [1,0,0,0,0,1]                 coins  2  [1,1,0,1,0,1]

                                Flip for easier coding

                    amount                                  amount
                    0 1 2 3 4 5                             0 1 2 3 4 5  
         coins  2  [1,0,1,0,1,1]       =>               1  [1,1,2,2,3,4] 
                5  [1,0,0,0,0,1]                 coins  2  [1,0,1,0,1,1]

        n is amount
        m is the length of coins
        Time: O(m * n)
        Space: O(n)
        '''
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(len(coins)-1, -1, -1):
            next_dp = [0] * (amount + 1)
            next_dp[0] = 1

            for amnt in range(1, amount+1):
                prev_coin = amnt - coins[i]
                if prev_coin >= 0:
                    next_dp[amnt] += next_dp[prev_coin]
                next_dp[amnt] += dp[amnt]

            dp = next_dp

        return dp[amount]


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        '''
        DP

        - at any given position, we subtract the current total by the current coin
            - if the current total is still positive, then we go to the index of the previously calculated total
        - we will also be working backwards, from the biggest coins and the smallest amounts

        EX: coin 1 at amount 4
            - current_amount = 4
            - subtract the current coin(1) => now current amount is 3
            - go to the third amount and add that value to the current position
            - but we also need to check the other possibilities of using the other coins
                - so look under it at same amount(4) at coin(2)
                - we add that
            - 3 + 1 = 4
            - 4 is what we put in the current position

                    amount
                    5 4 3 2 1 0
                1  [4,3,2,2,1,1] 
         coins  2  [1,1,0,1,0,1]
                5  [1,0,0,0,0,1]

        Flipped for eaasier coding
                    amount
                    0 1 2 3 4 5
                1  [1,1,2,2,3,4] 
         coins  2  [1,0,1,0,1,1]
                5  [1,0,0,0,0,1]

        n is amount
        m is the length of coins
        Time: O(m * n)
        Space: O(m * n)
        '''
        dp = [[0] * (amount + 1) for i in range(len(coins))]
        for row in dp:
            row[0] = 1

        for i in range(len(coins)-1, -1, -1):
            for amnt in range(1, amount+1):
                prev_coin = amnt - coins[i]
                if prev_coin >= 0:
                    dp[i][amnt] += dp[i][prev_coin]
                if i < len(coins) - 1:
                    dp[i][amnt] += dp[i+1][amnt]

        return dp[0][amount]


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        '''
        Recursive memoization

        n is amount
        m is the length of coins
        Time: O(m * n)
        Space: O(m * n)
        '''

        cache = {}

        def dfs(i, total):
            if total == amount:
                return 1

            if total > amount or i == len(coins):
                return 0

            if (i, total) in cache:
                return cache[(i, total)]

            # take coin, skip coin
            cache[(i, total)] = dfs(i, total + coins[i]) + dfs(i + 1, total)
            return cache[(i, total)]

        return dfs(0, 0)
