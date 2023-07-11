class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
        [1,2,3,4,2,6,4]
               |
        mid+1 > mid
        (ascending which means that the peak is to the right)
            left = mid+1
        mid+1 < mid
        (descending which means that the peak is somehwere in the left half)
            right = mid
        [1,2,3,4]
             |
              [4]

        [1,3,2,1]
             |
        [1,3,2]
           |
        [1,3]
         |
          [3]


        Time: O(logn)
        Space: O(1)
        '''
        l, r = 0, len(nums)-1

        while l < r:
            mid = (l+r)//2

            if nums[mid+1] <= nums[mid]:
                r = mid
            else:
                l = mid+1
        # peak = l
        return l
