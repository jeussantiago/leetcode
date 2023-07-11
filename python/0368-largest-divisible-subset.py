class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        '''
        - have to sort, this will allow us to compare the lower numbers first

        nums = [1,2,3,4,6]
        - create a dp to fill each index with the subset of the numbers are are divisible by 0
        - sorting helps since we only need to check the numbers < than the current index
        dp = [[1], [2], [3], [4], [6]]
        - go to the index before and check if the number at the nums[j] is divisible by the current num at nums[i] => nums[i] % nums[j] == 0
            - add that number at j to i
        [[1], [1,2], [1,3], [4], [6]]
        - we know that if a nums[i] % nums[j] == 0 then that means that the other numbers in nums[j] are also % == 0 to num[i]
        - so we can extend the nums[j] to i
        [[1], [1,2], [1,3], [1,2,4], [6]]
        - some numbers like 6 are % == 0 to nums like 2 and 3, but we don't want keep the longest divisible number so we need to put a check
        in place for the lengths
        [[1], [1,2], [1,3], [1,2,4], [1,3,6]]
        - check if len([1,2]) + 1 is longer than the current nums[i] which is [1,3,6]
            - its not so don't do anything
            - but if it was, we would replace the list at 6

        Time: O(n^2)
                    ; (nlogn) sorting
                    ; (n^2) going through combination of numbers
        Space: O()
                    ; (n) sorting
                    ; (n^2) dp
        '''

        # sort nums
        nums.sort()
        # create dp
        dp = [[num] for num in nums]

        # iterate over nums and previous indexes
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
                    dp[i] = dp[j] + [nums[i]]

        return max(dp, key=lambda x: len(x))
