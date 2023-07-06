class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        - binary search
        - if it returns a value then target is in value
        - if gets out of while loop then you ask if mid is lower than the target in which case
        the target would be place on the index after this mid index

        Contraints:
        - nums has to atleast have 1 number
        - nums contains distinct (no repeating numbers)

        Time: O(log n)
        Space: O(1)
        '''
        l, r, mid = 0, len(nums)-1, 0
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                r = mid-1
            else:
                l = mid+1
        
        #if out of the loop (haven't return the index of the target) b/c the target doesn't exist
        if target > nums[mid]:
            return mid+1
        return mid

