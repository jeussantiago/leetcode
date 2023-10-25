class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        '''
        Greedy
        [1,4,3,7,4,5] k=3

        - start off at k for both left and right pointers
        - at each position, test if the nums[left] < nums[right]
            - if thats the case, then the value in left is less than the value in right
            and you move the right pointer over
            - we do this b/c we want to keep track of the minimum value in the subarray
        - we explore every n position

        Time: O(n)
        Space: O(1)
        '''

        N = len(nums)
        left = right = k
        res = curr_min = nums[k]

        while left > 0 or right < N-1:
            # left < right
            if (nums[left-1] if left else 0) < (nums[right+1] if right < N-1 else 0):
                right += 1
                curr_min = min(curr_min, nums[right])
            else:
                left -= 1
                curr_min = min(curr_min, nums[left])

            res = max(res, curr_min * (right - left + 1))

        return res
