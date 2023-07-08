class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        - move the 2 (blue) to the end of the list
        - move the 0 (red) to the beginning of the list
        - don't touch the 1 (white)


        - if move the 0 to the beginning
            - swap left and current pointer
            - increase the current pointer by 1
        - if move the 2 to the end
            - swap right and current pointer
            - can't increase current pointer by 1, just decrement right pointer by 1
            (this makes sure that there is definitely a 2 in the right side)
            (at some point, right pointer will be less than current pointer which will get out of loop)
        - if 1 don't touch
            - don't move it
            - increase the current pointer by 1


        Time: O(n) where n is the size of the list
        Space: O(1)
        """

        left, mid, right = 0, 0, len(nums)-1
        while mid <= right:
            if nums[mid] == 0:
                #swap left and mid pointer
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 2:
                #swap right and mid pointer
                nums[right], nums[mid] = nums[mid], nums[right]
                #only decrement right pointer and don't increase mid pointer(this makes sure that loop ends at some point)
                right -= 1
            else:
                #white (1)
                mid += 1
















