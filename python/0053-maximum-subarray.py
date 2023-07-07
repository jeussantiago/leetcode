class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        Kadane's Algorithm:
        # - keep track of the current max number and the previous current max numbers
        # - get the max of the two
        # - move the subarray start only when the current max number is bigger than the previous amx number

        - get the current max number by comparing the current number and the addition of the current number and teh previous current max number
        - this way, you can always check the what the max number is and move the subarray to a new start position when the cur_num is bigger than the previous cur_num
        - we compare the number alone to see if we need to start a new subarray since the numebr itself is just bigger
        - we compare it to the number + the added curr_sum to see if we want to continue the subarray
        [-2,1,-3,4]
        curr_num = -2
        curr_num = 1  res = 1 (start of a new subarray)
        curr_num = -2 res = 1
        curr_num = 4  res = 4 (start of a new subarray)

        Time: O(n)
        Space: O(1)
        '''

        max_sum, curr_sum = float('-inf'), 0
        for num in nums:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(curr_sum, max_sum)
        return max_sum
