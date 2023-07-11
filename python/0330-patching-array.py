class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        '''
        [1,2,5] ; n=10

        range
        [0,0] -> [0,1] -> [0,3]
        - we add the current num to the upper end of the range
                ( - add 1, then added 3 )
        - we can't add 5 because that would skip over 4

        - can only add a number if it is (curr_num <= upper_range + 1)
            upper_range += curr_num
            - go to next num

        - otherwise
            - add the next number of the upper range to itself
            (if [0,3] then 3 + (upper_range + 1) => 3 + (3+1) => 3 + 4 = 7)
            - this simulates us adding 4 to the nums and would now cover everything in the current range

            - increase the patches count + 1
            - don't increase the current num on cause we still havent processed that

        Time: O(n)
        Space: O(1)
        '''

        i, M, upper_range, res = 0, len(nums), 0, 0
        while upper_range < n:
            if i < M and nums[i] <= upper_range + 1:
                upper_range += nums[i]
                i += 1
            else:
                upper_range += (upper_range + 1)
                res += 1

        return res
