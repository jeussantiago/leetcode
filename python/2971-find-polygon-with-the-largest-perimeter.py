class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        '''
        Time: O(nlogn)
            ; (nlogn) sort
            ; (n) prefix sum
        Space: O(1)
        '''
        nums.sort()
        running_sum = 0
        res = -1
        for num in nums:
            if num < running_sum:
                res = running_sum + num
            running_sum += num

        return res
