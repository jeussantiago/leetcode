class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        '''
        - only need current index
        - base case: if ind > len(arr): return 0

        - from our starting index, we want to iterate up to min(ind + k, len(arr))
            - get the max value in the subarray of arr[ind:curr_k + 1]
            - get the current size of the subarray = curr_k - ind + 1

            - the current value, simulating that this is the end of the subarray = max_val_sub_arr * subarray_size
            - recurse into next subarray

            - add these two values
            - keep track of the running max 

        - caching:
            - if we visit an ind at the start of the function, then we shouldn't visit the ind
            at the start of the function again until we start a new subarray
            - in that case, we have already calculated it, and thus, we don't need to calculate it
            again.

        Time: O(n * k)
        Space: O(n * k)
        '''

        N = len(arr)

        @cache
        def dfs(left):
            if left == N:
                return 0

            res = 0
            for right in range(left, min(left + k, N)):
                max_sub_arr_val = max(arr[left:right + 1])
                subarray_size = right - left + 1
                subarray_total = max_sub_arr_val * subarray_size

                curr_total = subarray_total + dfs(right + 1)
                res = max(res, curr_total)

            return res

        return dfs(0)
