class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        binary search
        [4,5,6,7,0,1] search 7
        [6,7,0,1,2,3] search 7
        - if left < mid
            - if target < left or target > mid
                l = mid+1
            - if target > left
                r = mid-1
        - if right > mid
            - if target > right or target < mid
                r = mid-1
            - if target < right
                l = mid+1

        Time: O(log n)
        '''

        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]:
                if target < nums[l] or target > nums[mid]:
                    l = mid+1
                else:
                    r = mid-1
            else:
                if target > nums[r] or target < nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
        return -1

