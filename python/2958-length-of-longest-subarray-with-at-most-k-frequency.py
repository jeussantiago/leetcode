class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        '''
        Two Pointer

        Time: O(n)
        Space: O(1)
        '''

        freq = collections.defaultdict(int)
        left = 0
        longest_subarray = 0
        for right in range(len(nums)):
            freq[nums[right]] += 1
            # k cant be <= 0
            # we don't put a condition to check left < right
            # b/c left should never go past the right index anyways
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1

            longest_subarray = max(longest_subarray, right - left + 1)

        return longest_subarray
