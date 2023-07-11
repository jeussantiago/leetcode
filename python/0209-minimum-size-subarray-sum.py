class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        2 pointers
        while right <= len(nums)
        - if total >= target and left < right
            (met result conditions)
            - save the minimum length subarray to the results
            - move left pointer +1
        - total < target or left >= right
            - move right pointer +1

        - when right gets out of bounds, we need a condition for iterating only left but still checking if sum is over target

        - maybe have another while loop


        Time: O(n)
        Space: O(1)
        '''

        N = len(nums)
        res = float('inf')
        l, r = 0, 1
        total = nums[0]
        while r <= N:
            if l < r and total >= target:
                res = min(res, (r-l))
                total -= nums[l]
                l += 1
            else:
                tmp = nums[r] if r < N else 0
                total += tmp
                r += 1

        if res == float('inf'):
            res = 0

        return res
