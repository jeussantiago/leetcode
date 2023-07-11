class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        '''
        [2,9,4]

        - go through the indexes of the cost
            - val_at_current_index = dp[min_val (not including current index)] + current index val

        [1,5,3]

        Time: O(n * k^2)
        Space: O(k)
        '''
        n = len(costs)
        k = len(costs[0])
        dp = costs[0]

        for i in range(1, n):
            new_costs = [0] * k
            for j in range(k):
                dp_min = min(dp[:j] + dp[j+1:])
                new_costs[j] = dp_min + costs[i][j]
            dp = new_costs
            print(dp)

        return min(dp)
