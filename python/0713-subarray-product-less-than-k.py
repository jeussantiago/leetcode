class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        '''
        Sliding Window

        Time: O(n)
        Space: O(1)
        '''

        # base case: if k = 0, pointers are always going to be on the same spot
        # since min value of nums is 1. In the same sense, if k = 1, we can't
        # reach it since value has to be <, not <= to k.
        if k <= 1:
            return 0

        subarrays_less_than_k = 0
        product = 1
        left = 0
        for right in range(len(nums)):
            product *= nums[right]

            while left < right and product >= k:
                product //= nums[left]
                left += 1

            # left and right indexes might be on same position
            # but num value/product might be >= k
            if product < k:
                subarrays_less_than_k += (right - left + 1)

        return subarrays_less_than_k
