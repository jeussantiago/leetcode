class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        - start at len(nums) - 2 (second to last)and serach leftwards
        - find first descending number from the right (right to left)-> just compare nums[i] and nums[i+1]
        - another pointer that starts at len(nums) - 1 (very last) and traverse until find the first number that is greater than the left pointer
        - swap left and right pointer
        - reverse the order of the elements to the right of the left pointer

        [1,3,2] left: 1 (index: i-1)  right: 2
        [2,3,1]
        [2.1.3] (reversed after first pointer)
        """
        def swap(l, r):
            nums[l], nums[r] = nums[r], nums[l]

        def reverse(i):
            nums[i:] = nums[len(nums)-1 : i-1 : -1]
        

        #find first descending number from the right
        left = len(nums) - 1
        while left > 0 and nums[left-1] >= nums[left]:
            left -= 1

        if left == 0:
            nums.reverse()
            return

        #traverse from right until find the first number that is greater than the left pointer
        right = len(nums) - 1
        while nums[right] <= nums[left-1]:
            right -= 1

        #swap left and right pointer
        swap(left-1, right)

        #reverse the order of the elements to the right of the left pointer
        reverse(left)




        
