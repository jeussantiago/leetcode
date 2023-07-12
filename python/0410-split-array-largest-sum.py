class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        '''
        - the minimum the result can be is max(nums)
        - the maximum the result can be is sum(nums)

        - binary search on the range of possible values:
            - left_boundary = min_result_can_be = max(nums)
            - right_boundary = max_result_can_be = sum(nums)

            - mid:
                - can we take the array and split into k groups such that the largest sum of the k groups
                    - is <= mid:
                        - new_minimum_possible_range found
                        - left_boundary = mid
                    - is > mid:
                        - right_boundary = mid - 1
                        - res = mid

                - splitting arr into k groups
                Greedy:

                    - we keep adding the current num to the current subarray
                    - if the current num brings the sum of the current subaray to over the mid, then start a new subarray
                    - Even if we get through the array and we still have a few more subarrays needed, its
                    fine b/c we are able to split the other subarrays
                        - if those subarrays are < mid, then splitting them to fill in the k subarays is definitely going
                        to be < mid
                    - the only time its not ok is if we run out of k subarrays and the pointer in array hasn't reached the end
                    EX: [7,2,5,10,18] ; mid = 27 ; k = 3

        S is the sum of nums
        n is the length sof nums
        Time: O(nlogS)
        Space: O(1)
        '''

        def can_split_into_k_groups(largest):
            sub_array_count = 1
            curr_sum = 0
            for num in nums:
                curr_sum += num
                if curr_sum > largest:
                    sub_array_count += 1
                    curr_sum = num

            return sub_array_count <= k

        left_boundary, right_boundary = max(nums), sum(nums)
        res = right_boundary
        while left_boundary <= right_boundary:
            mid = (left_boundary + right_boundary) // 2

            if can_split_into_k_groups(mid):
                res = mid
                right_boundary = mid - 1
            else:
                left_boundary = mid + 1

        return res
