class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        '''
        Greedy

        - count 1's
        - if hit 0, 
            - total the previous 1 count and the current 1 count
            - prev 1 count = curr 1 count
            - reset curr 1 count = 0

        edge case: 
        - repeating 0
        [0,1,1,1,0,0,0,1,1,0,1]

        - all 1s
        [1,1,1,1]


        Time: O(n)
        Space: O(1)
        '''
        res = 0
        prev_cnt, curr_cnt = 0, 0
        for num in nums:
            if num == 1:
                curr_cnt += 1
            else:
                res = max(res, prev_cnt + curr_cnt)
                prev_cnt = curr_cnt
                curr_cnt = 0

        if curr_cnt == len(nums):
            return len(nums) - 1

        if curr_cnt or prev_cnt:
            res = max(res, prev_cnt + curr_cnt)

        return res
