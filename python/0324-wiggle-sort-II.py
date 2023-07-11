class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        [1, 1, 1, 4, 5, 6]
        -------
        [1, 6, 1, 1, 6, 4]
        [1, 6, 1, 5, 6, 4]
        [1, 6, 1, 5, 6, 4]
        --------
        [1, 6, 1, 5, 6, 4]
        [1, 6, 1, 5, 6, 4]
        [1, 6, 1, 5, 1, 4]
        --------
        --------
        [1, 6, 1, 5, 1, 4]

        Time: O(nlogn)
        Space: O(n)
        """
        nums_copy = nums.copy()
        nums_copy.sort()

        N = len(nums)
        i, r = 1, N - 1
        while i >= 0:
            for step in range(i, N, 2):
                nums[step] = nums_copy[r]
                r -= 1

            i -= 1

        print(nums)
