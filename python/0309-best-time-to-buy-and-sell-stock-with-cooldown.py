class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        dfs

        - if you buy
            - subtrack profit -> -prices[i]
            - can go to next index, since the only options able to do are
                - sell (increase in profit)
                - cooldown (profit stays the same)

        - if you sell
            - add profit -> + profit[i]
            - MUST have a cool down day, increase index by 2 (skip a day) - profit stays the same
            - have only 2 options after the skipped day
                - buy (deecrease in profit)
                - cooldown (profit stays the same)

        - Time complexity of this algorithm is O(2^n)
        - Can use extra memory for a cache to decrease time complexity

        cache -> key=(index, buyingState) ; value=profit
        buyingState -> 1=buying, 0=selling

        w/ cahce of problem
        Time: O(2 * n) there are 2 * n possible coimbinations in cache => got 2n b/c (index, buyingState) == index there are n
            choices and 2 possible buyingStates, buying and selling
            : O(n)
        Space: O(2 * n)
            : O(n)
        '''

        cache = {}

        def dfs(ind, isBuying):
            if ind >= len(prices):
                return 0

            if (ind, isBuying) in cache:
                return cache[(ind, isBuying)]

            if isBuying:
                buyProfit = dfs(ind + 1, not isBuying) - prices[ind]
                cooldownProfit = dfs(ind + 1, isBuying)
                cache[(ind, isBuying)] = max(buyProfit, cooldownProfit)
            else:
                # selling
                sellProfit = dfs(ind + 2, not isBuying) + prices[ind]
                cooldownProfit = dfs(ind + 1, isBuying)
                cache[(ind, isBuying)] = max(sellProfit, cooldownProfit)

            return cache[(ind, isBuying)]

        return dfs(0, True)
