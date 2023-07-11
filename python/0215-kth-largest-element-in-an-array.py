class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        Quick Select:

        k = 2
        [3,2,1,5,6,4]
        - every value in array is <= to every value in the right side of the aray
        - ideally we could split it in half everytime, but we can't(this is why worst case time compex is n^2)
        - we could do python's random but since we can't control anything, we might as well just pick the value 
        on the right (in this example it is 4)
        - moving the pieces will be done in-place, no extra memory
        [3,2,1] | [5,6] | [4]
        - pivot point = 3
        (everything before pivot is < nums[-1] ; everything after excep the last element is > nums[-1])

        - now swap the last element and the pivot position
        [3,2,1] | [4] | [6,5]
         0 1 2     3     4 5
        k = 2
        len(nums) - 2 = 4
        - this number tells us that the kth largest number is in the right side of the array
        - if the number is == pivot, then that is the kith largest
        - if its greater than the pivot, then the kth largest is in the right side
        - if its less than the pivot, then the kth largest is in the left side

        [6,5]
        - swap with pivot point
        => [_, _, _, _,] | [5] | [6]
        len(nums) - k = 4
        4 == pivot
            - answer is value in pivot point => 5

        Time: avg O(n) worst O(n^2)
        Space: O(n)
        '''
        # turn k into its position in the nums array if it were sorted
        k = len(nums) - k
        start, end = 0, len(nums) - 1

        def helper(start, end):
            if start > end:
                return nums[k]

            pivot = start
            pivotVal = nums[end]
            for i in range(start, end):
                if nums[i] <= pivotVal:
                    nums[pivot], nums[i] = nums[i], nums[pivot]
                    pivot += 1
            nums[pivot], nums[end] = nums[end], nums[pivot]

            if pivot == k:
                return nums[pivot]
            elif pivot < k:
                start = pivot + 1
            else:
                end = pivot - 1

            return helper(start, end)

        return helper(start, end)
