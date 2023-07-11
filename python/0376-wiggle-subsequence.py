class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        '''
        This problem's greedy soluution is the same as finding the number of peaks and valleys in the in a list
        - if the nums keep rising, it is going towards the peak which is the highest number
            - when the direction chnges, then youve reached the peak
        - if the nums keep decreasing, it is going towards the valley which is the lowest num
            - when the direction change thne you've reached the valley

        Time: O(n)
        Space: O(1)
        '''

        N = len(nums)
        res = 1
        # 1 means was increasing, -1 means was decreasing
        prev_direction = None

        if N < 2:
            return N

        for i in range(1, N):
            if (
                nums[i] > nums[i-1] and
                (prev_direction == -1 or prev_direction == None)
            ):
                # peak
                prev_direction = 1
                res += 1

            elif (
                nums[i] < nums[i-1] and
                (prev_direction == 1 or prev_direction == None)
            ):
                # valley
                prev_direction = -1
                res += 1

        return res
