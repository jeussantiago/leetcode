class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
          2 3 -2 4  
         [0,6,-6,0]
         - 2 * 3 = 6
            (max(6, 0))
        - 3 * (-2) = -6
        - 6 * (-2) = -12
        - put in the slot the higher number between the two
            - choosing the first means that you are starting a new subarray
            - choosing the second means that you are continuing the subarray
        - but the answer is the Max(
            - new subarray
            - continuing subarray
            - the already exisiting answer
            - the current number
        )
        [0,6,-6,-8]
        -2 * 4 = -8
        -6 * 4 = -24

        - keep track of the max and the min in case of many negatives
        [-1,-2,-9,-6]
        max [-1,2,18,-54]
        min [-1,-2,-9,108]

        Time: O(n)
        Space: O(n)
        '''
        # nums = [-2,3,-4]
        # output: 3 ; expected: 24
        # nums = [-1,-2,-9,-6]
        # output: 54 ; expected: 108

        n_max = 1
        n_min = 1

        res = nums[0]
        for num in nums:
            tmp_max = n_max * num
            tmp_min = n_min * num

            n_max = max(tmp_max, tmp_min, num)
            n_min = min(tmp_max, tmp_min, num)

            res = max(res, n_max)

        return res
