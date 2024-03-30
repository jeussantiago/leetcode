class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        '''
        - we might be counting more subarrays then there actually exist 
        that contain k distinct numbers.
        - the helper function calculates the number of subarrays where
        k_unique <= k, however, we only want k
        - solution is to get the number of subarrays where k_unique <= k-1
            - in this way, we can remove the difference in the subarrays

        Time: O(n)
        Space: O(n)
        '''
        return self.helper(nums, k) - self.helper(nums, k - 1)

    def helper(self, nums, k):
        '''
        count the number of subarrays where there are k distinct numbers
        '''
        subarray_cnt = 0
        left = 0
        unique_num_cnt = 0
        freq = collections.defaultdict(int)
        for right in range(len(nums)):
            if freq[nums[right]] == 0:
                unique_num_cnt += 1

            freq[nums[right]] += 1

            while unique_num_cnt > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    unique_num_cnt -= 1

                left += 1

            subarray_cnt += (right - left + 1)

        return subarray_cnt
