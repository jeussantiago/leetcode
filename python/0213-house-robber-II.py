class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        [1,2,3,1]
        - we can treat this problem similarly ot House Robber I
        - instead of dealing with a circular list, we can treat it as 2 normal list
        - run House Robber I on nums[0:i-1] ([1,2,3]) and on nums[1:n] ([2,3,1])
        - the solution is the max of it


        House Robber I:
        - the first value in the array is the nums[0]
        - the second is the max(nums[0], nums[1])
        - you can decide to take the max(numes[i-1], nums[i] + nums[i-2])

        Time: O(n), we do two runs through the list 
        Space: O(n), created a dp array, but can do this without creating an array

        '''

        def houseRob(nums):
            dp = [0] * (N-1)
            if len(dp) == 1:
                return nums[0]

            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, N-1):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            return dp[-1]

        N = len(nums)
        if N == 1:
            return nums[0]

        left = houseRob(nums[:N-1])
        right = houseRob(nums[1:])

        return max(left, right)
