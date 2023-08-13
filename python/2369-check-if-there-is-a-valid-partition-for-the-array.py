class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        '''
        DP (space optimization)

        - we can convert the recursive solution by having an array of bool values
        nums = [4,4,4,5,6]

        dp = [_,_,_,_,_]
        - we will work backwards to replicate the dfs solution
        - we have to fill in the last three values
            - the very last value [-1] will be false no matter what
            - the second to last value depends on if its the same number as last
            - third value is if the rest of the numbers equal each other or are increasing by +1
        dp = [_,_,T,F,F]

        - at each position in the nums that isn't filled, starting backwards,
            - check if the number follows the valid conditions of a subarray
                - if 2 consecutive valid
                    - take the value at +2 of the current position
                - 3 consecutive or 3 increasing
                    - take value at +3 of current position

        - continuing dp, current_pos=1
            - [4,4] valid for 2 consecutive
                - take bool value stored at position=3 (i+2)
            - other conditions are false
        dp = [_,F,T,F,F]
            - current pos = 0
            - [4,4] 2 consecutive valid
                - take bool at position=2 (i+2) - True
            - [4,4,4] 3 consecutive valid
                - take bool at position=3 (i+3) - False

            - if position is True, keep it True (don't turn to false)

        dp = [T,F,T,F,F]

        Time: O(n)
        Space: O(n)

        - we notice that we really only need to keep in storage the last three positions
        - this is how we turn space usage from (n) to (1)
        dp = [T,F,F]
        dp = [F,T,F]
        dp = [T,F,T]

        Time: O(n)
        Space: O(1)
        '''
        # consecutive 2
        last_sec = (nums[-1] == nums[-2])
        # make sure theres enough numbers
        if len(nums) == 2:
            return last_sec
        # consecutive 3 or increasing +1
        last_third = (nums[-3] == nums[-2] == nums[-1]
                      or nums[-3] + 1 == nums[-2] == nums[-1] - 1)

        dp = [last_third, last_sec, False]

        for i in range(len(nums) - 4, -1, -1):
            cur = False
            # consecutive 2
            if nums[i] == nums[i + 1]:
                cur = dp[1]
            # consecutive 3
            if nums[i] == nums[i + 1] == nums[i + 2]:
                cur = cur or dp[2]
            # increasing 1
            if nums[i] + 1 == nums[i + 1] == nums[i + 2] - 1:
                cur = cur or dp[2]

            dp = [cur, dp[0], dp[1]]

        return dp[0]


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        '''
        DFS - memoization

        Time: O(n)
        Space: O(n)
        '''
        cache = {}

        def dfs(i):
            if i == len(nums):
                return True

            if i in cache:
                return cache[i]

            res = False
            # 2 consecutive
            if i < len(nums) - 1 and nums[i] == nums[i + 1]:
                res = dfs(i + 2)
            # 3 consecutive
            if i < len(nums) - 2 and nums[i] == nums[i + 1] == nums[i + 2]:
                res = res or dfs(i + 3)
            # 3 increasing by 1
            if i < len(nums) - 2 and nums[i] + 1 == nums[i + 1] == nums[i + 2] - 1:
                res = res or dfs(i + 3)

            cache[i] = res
            return res

        return dfs(0)
