class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        '''
        prices    [5, 11, 3, 50, 60, 90]
                k
        profit  0 [0, 0,  0,  0  0,  0 ]
                1 [0, 6,  6, 47, 57, 87] 
                2 [0, 6,  6, 53, 63, 93]

        profit[k][day] = max(
            profit[k][d-1],
            - not buying yet and taking the previous days profit
            prices[d] +  max( -prices[d] + profit[k-1][d] )
                            => d =  0: -5 + 0 = -5
                                    1: -11 + 6 = -5
                                    2: -3 + 6 = 3
                                    3: -50 + 47 = -3
                                    4: -60 + 57 = -3
            - (sell price + max((-) buy price + first sell profit))
            - we have it in max b/c the second sell price is a constant between all days
                - to mazimize that number, we want the most money left for us after we sell our
                first stock and buy our second. so we go through the previous days
        )

        ** modified version - previous version time limit exceeded

        Time: O(kn)
        Space: O(n)

        https://youtu.be/Pw6lrYANjz4
        '''
        N = len(prices)
        prevProfit = []
        currProfit = [0] * N

        for t in range(k):
            maxPrevProfit = -prices[0]  # -prices[d] + profit[k-1][d]
            prevProfit = currProfit.copy()
            for i in range(1, N):
                currProfit[i] = max(
                    currProfit[i-1],
                    (prices[i] + maxPrevProfit)
                )
                maxPrevProfit = max(
                    maxPrevProfit, (-prices[i] + prevProfit[i]))

        return currProfit[-1]
