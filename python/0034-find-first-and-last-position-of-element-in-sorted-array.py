class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''
        - binary search to find the target in the array
        - if serach returns a value then traverse left to find first position and traverse right to find the right position]

        contraints:
        - length of nums can be 0
        - nums is non-decreasing

        Time: O(log(n) + n) = O(log n) where n is the length of the array
        Space: O(1)
        '''

        def binarySearch(target, nums):
            l, r = 0, len(nums)-1
            while l <= r:
                mid = (l+r)//2
                # print(l, mid, r, nums[l], nums[mid], nums[r])
                if nums[mid] == target:
                    return mid
                elif target < nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            return -1
                


        if nums:
            target_index = binarySearch(target, nums)
            if target_index == -1:
                return [-1, -1]
            
            l, r = target_index, target_index
            while l > 0 and nums[l-1] == target:
                l -= 1
            while r <= len(nums)-2 and nums[r+1] == target:
                r += 1
            return [l,r]

            
        else:
            return [-1, -1]
    