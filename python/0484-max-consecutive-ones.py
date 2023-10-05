class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        '''
        Time: O(n)
        Space: O(1)
        '''
        max_one_count = 0
        curr_one_count = 0
        for num in nums:
            if num == 0:
                max_one_count = max(max_one_count, curr_one_count)
                curr_one_count = 0
            else:
                curr_one_count += 1

        max_one_count = max(max_one_count, curr_one_count)
        return max_one_count
