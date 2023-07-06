class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        - array is unsorted
        -length of array is between 0 and 50
        
        - another approach considers that the end result doesn't matter in terms of order, it just cares about the return number
        - checks if the current number==val, swaps the current number with the last number
        - reduce length of array
        Time: O(n)
        Space: O(1)
        '''
        l = 0
        r = len(nums)
        while l < r:
            if nums[l] == val:
                #take last elements value and reduce array size
                nums[l] = nums[r-1]
                r -= 1
            else:
                #number not val, increase left pointer
                l += 1
        return r