class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        n is the length of cost
        Time: O(n)
        Space: O(1)
        '''
        # top stair
        cost.append(0)

        for i in range(2, len(cost)):
            two_step = cost[i - 2]
            one_step = cost[i - 1]

            cost[i] += min(one_step, two_step)

        return cost[-1]
