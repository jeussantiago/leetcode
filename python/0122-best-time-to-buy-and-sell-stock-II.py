class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Greedy approach:

        [7,6,5,5,1,5,5,6,7,5,4,3,6,4]

        - don't do anything if profit is negative
            - so take max of 0 and difference

        - if the numbers are >= day i and day i-1 
            - we can continuously add the profit valus

        Time: O(n)
        Space: O(1)
        '''
        if len(prices) == 1:
            return 0

        profit = 0
        for i in range(1, len(prices)):
            profit += max(0, (prices[i] - prices[i-1]))

        return profit
