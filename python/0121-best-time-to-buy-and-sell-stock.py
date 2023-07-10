class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        [7,4,2,5,3,6,1,4]

        - lowest_price = initially be float inf but whenever you see a price that is lower than this, meaning that it goes
        negative, we can update this lowest price
        - otherwise, the price is bigger than the lowest price so we can subtract the current indx price from the lowest price,
            - save whichever is bigger into a value

        Time: O(n)
        Space: O(n)
        '''

        lowest_price = prices[0]
        profit = 0

        for price in prices:
            lowest_price = min(lowest_price, price)
            profit = max(profit, price - lowest_price)

        return profit
