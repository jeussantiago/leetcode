class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        '''
        [1] [3,1,5,8] [1]

        - treat it backwards
            - what if the index you were at, you popped it last
            - then treat the left and right side as sub problems

        - Ex: index 2 = 5
        - left, right = 1, len(nums) - 2
        - pop 5 last, thsi means that you would multiple by 1 and 1, (l-1 and r-1)
        - then treat the left and right side as sub problems
        [1] [3,1,5,8] [1]
        - [3,1] would be a subproblem
            - l, r = 3, 1
            - for example, if you pop 1, l-1 * 1 * r - 1 == 1 * 1 * 5 (since 5 is to the right of the current number)
                - we can multiply by 5 because it is popped last
            - solve the sub problem of [3]
        - [8] would be a sub problem
            - similar situation for [8] since 5 is on the left

        - we would need to run through the entire nums so that means that there are many combinations for l and r pointers
        - save it to a cache, if the l and r have been visited then just return that

        Time: O(n^3)
        Space: O(n^2)
        '''
        nums = [1] + nums + [1]

        cache = {}

        def dfs(l, r):
            if l > r:
                return 0

            if (l, r) in cache:
                return cache[(l, r)]

            max_coin_total = 0
            for i in range(l, r+1):
                coin_total = nums[l-1] * nums[i] * nums[r+1]
                # left sub-problem
                coin_total += dfs(l, i-1)
                # right sub-problem
                coin_total += dfs(i+1, r)

                max_coin_total = max(max_coin_total, coin_total)

            cache[(l, r)] = max_coin_total
            return cache[(l, r)]

        return dfs(1, len(nums)-2)
