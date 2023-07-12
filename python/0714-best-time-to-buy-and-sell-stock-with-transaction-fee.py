class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        '''
        [1,3,2,8,4,9], fee = 2
        -1, -4 0 

        Time: O(n)
        '''

        hold, profit = -prices[0], 0
        for i in range(len(prices)):
            hold = max(hold, profit - prices[i])
            profit = max(profit, hold + prices[i] - fee)

        return profit
