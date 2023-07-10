class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        - greedy algorithm
        - save values in list

        - sort the list
        - grab 2 highest values

        Time: O(n)
        Space: O(n)

        https://youtu.be/Pw6lrYANjz4

        '''

        if not prices:
            return 0

        first_buy, first_profit = float('inf'), 0
        second_buy, max_profit = float('inf'), 0

        for price in prices:
            first_buy = min(first_buy, price)
            first_profit = max(first_profit, price-first_buy)
            second_buy = min(second_buy, price-first_profit)
            max_profit = max(max_profit, price-second_buy)

        return max_profit
