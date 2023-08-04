class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        '''
        - taking the mean doesn't work for 
        [1,1,10] => mean=4 => num_moves = 12
                 => but as we can see, we can turn the 10 to a 1 and the min_num_moves=9
        - can take take the median
            - also works for even length nums

        Time: O(nlogn)
            ; (nlogn) sort
            ; (1) get median value
            ; (n) take the num difference from median and sum
        Space: O(n)
            ; (n) python sorting
        '''

        nums.sort()
        n = len(nums)
        median = nums[n//2]
        return sum(abs(median - num) for num in nums)
