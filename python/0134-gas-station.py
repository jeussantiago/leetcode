class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
        gas = [1,2,3,4,5]
        cost = [3,4,5,1,2]
        diff = [-2,-2,-2,3,3]
                 X  X  X O
        total = [-2,0,0,3,6]

        Greedy Approach
        - tank + gas - cost
        - if the toal is < 0, then move the starting ind to whatever is next
        - taking advantage of the fact that there is only one unique solution
        - so whichever position the ind is at the end is the solution since at the end it'll be >= 0


        Time: O(N)
        Space: O(1)
        '''

        if sum(gas) < sum(cost):
            return -1

        tank = 0
        starting_ind = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]

            if tank < 0:
                starting_ind = i + 1
                tank = 0

        return starting_ind
