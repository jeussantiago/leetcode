class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        '''
        nums = [2,5,6,0,0,1,2], target = 3
        [2,5,6,0,0,1,2]
        if l < mid: (majority of items are on the left since the array is pivoted somewhere in the first half of the array)
            [0,1,2,4,4,4,5,6,6,7] => [4,4,4,5,6,6,7,0,1,2] mid=6, left=4 ; pivoted at index 2
            #target outside of range
            target < l or target > mid:
                l = mid+1
            target > l and target < mid:
                r = mid+1
        else: # l > mid (majority of items are on the right since the array is pivoted somewhere in the second half of the array)
        [0,1,2,4,4,4,5,6,6,7] => [6,6,7,0,1,2,4,4,4,5] mid=3, left=6 ; pivoted at index 8
            #target within bounds of array
            target > r or target < mid:
                r = mid-1
            target < r and target > mid



        Time: O(logn)
        Space: O(1)
        '''

        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return True

            if nums[mid] == nums[r]:
                # list might be pivoted at a repeating number, go to next index if that is the case
                r -= 1
            elif nums[l] <= nums[mid]:
                if target < nums[l] or target > nums[mid]:
                    l = mid+1
                else:
                    r = mid-1
            else:
                if target > nums[r] or target < nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
        return False
