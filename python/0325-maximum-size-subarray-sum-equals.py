class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        '''
        Prefix Sum:
        nums = [1,-1,5,-2,3] ; k = 3

        prefixSum = [1, 0, 5, 3, 6]

        - if the current sum == k
            - at that index, we can say that the current longest is the current_indx + 1

        nums = [-2,-1,2,1], k = 1
        prefixSum = [-2, -3, -1, 0]

        - at every position we can check how much we need remaining when we subtract => k - curr_prefixSum
        - if that remainder was already calculated in the prefix sum,
            - then we can get the index of the remainder and check for the longest subarray
            (
                curr_i = 2
                curr_prefixSum = -1

                curr_prefixSum - k = (-1) - 1 => remaining = -2
                remaing is already in prefixSum, so we go to that position and get the index
            )

        - we can store the prefixSum and the index of the prefixSUm in a hash map so that we can check in O(1) time

        Time: O(n)
        Space: O(n)
        '''

        prefixSums, curr_prefixSum = {}, 0
        longest_substring = 0
        for i, num in enumerate(nums):
            curr_prefixSum += num
            if curr_prefixSum == k:
                longest_substring = i + 1

            remaining = curr_prefixSum - k
            if remaining in prefixSums:
                longest_substring = max(
                    longest_substring, i - prefixSums[remaining])

            # prefix sums can appear multiple times since the arr is not sorted
            # we want the longest subarray, so we don't want to overwrite the previous index of the sum
            # this will result in a bigger index, but we want the smallest
            # prefix sums that appear first are the smallest so we only add the index if the prefix sum isn't already in the dict
            if curr_prefixSum not in prefixSums:
                prefixSums[curr_prefixSum] = i

        return longest_substring
