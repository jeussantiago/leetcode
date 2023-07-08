class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        each number can have max 2 in array
        - ends of the number
        - only keep the ends
        
        insert at left point only when characters are different on both sides
        (we're only insert the ends of the number sequence)
        if position on left is < 0 or position on left is a different number:
            - replace the current left pointer with the current number
            - increase left pointer by 1
        if position on right is > len(nums) or position on the right is a different number:
            - replace the current left pointer with the current number
            - increase left pointer by 1
        -always increase current index 
        [0,0,1,1,1,1,2,3,3] 0, 0
                     |   |
        [0,0,1,1,2,3,3,3,3]

        Time: O(n) length of the nums array
        Space: O(1)
        '''

        leftPointer = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1] or i == len(nums)-1 or nums[i] < nums[i+1]:
                nums[leftPointer] = nums[i]
                leftPointer += 1
        #k
        return leftPointer