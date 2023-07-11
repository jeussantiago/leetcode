class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Method 3:

        [1,2,3,4,5,6,7], k = 3
        - reverse nums
        [7,6,5,4,3,2,1]
        - reverse the [0:k]
        [5,6,7,4,3,2,1]
        - reverse the [k+1:end]
        [5,6,7,1,2,3,4]

        Time: O(n)
        Space: O(1)
        """
        N = len(nums)

        # k might be longer than length of nums so you don't want to do repeating cycles
        k = k % N

        # Method 3

        def reverse(nums, l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1
            return nums

        # reverse nums
        l, r = 0, N-1
        nums = reverse(nums, l, r)

        # reverse [0:k] positions
        l, r = 0, k-1
        nums = reverse(nums, l, r)

        # reverse [k] positions
        l, r = k, N-1
        nums = reverse(nums, l, r)


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Method 1:
        - pop
        - insert at beginning

        Time: O(n)
        Space: O(1)

        Method 2 (personally favorite solution):

        - use extra memory, create another array thats the same length as nums
        - at every position in nums, calculate what the new position would be in the new array
            - (current_pos_i + k) % len(nums) => new position in new array

        Time: O(n)
        Space: O(n)
        """
        # Method 2
        tmp = [nums[i] for i in range(N)]

        for i in range(N):
            nums[(i + k) % N] = tmp[i]
