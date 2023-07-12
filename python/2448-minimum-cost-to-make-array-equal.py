class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        '''
        nums = [1,3,5,2], cost = [2,3,1,14]

        - ideal num somewhere in the range of min(nums) and max(nums)
            range(min(nums), max(nums) + 1)
            - in this case: 1 - 5

        Binary search

        - bottom of slope is the minimum total cost
        - using 2 positions to figure out the direction of the slope
            - compare Cost(i) and Cost(i + 1)

        if cost(i) < cost(i + 1)
            - min total cost should be to the left
            - right = mid
            (we only to mid inset of mid -1 since since the right position can be part of the solution set)

        if cost(i) >= cost(i + 1)
            - min cost somewhere to the right
            - left = mid + 1

        n is the length of nums
        k is the range of the min nums and max nums
        Time: O(nlogk)
        Space: O(1)
        '''

        def getCost(base):
            return sum(abs(base - num) * c for num, c in zip(nums, cost))

        left, right = min(nums), max(nums)
        minCost = getCost(nums[0])  # default minCost

        while left < right:
            mid = (left + right) // 2
            cost1, cost2 = getCost(mid), getCost(mid + 1)

            # since we are always going towards the bottom of the parabola graph
            # the 2 values are always going to be less than the previous minCost value
            # thats why we aren't even comparing it
            minCost = min(cost1, cost2)

            if cost1 < cost2:
                right = mid
            else:
                left = mid + 1

        return minCost
