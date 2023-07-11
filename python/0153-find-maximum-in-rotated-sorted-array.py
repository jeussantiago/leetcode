class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        [2,3,4,5,6,7,0,1]
        - have  left and right pointers
        - find mid
        [2,3,4,5,6,7,0,1]
                 |
                  [7,0,1]
                     |
                  [7]

        [6,7,0,1,2,3,4,5]
                 |
        [6,7,0,1]
             |
        [6,7]


        mid = 6
        if left >= right
            (want to search the right side of the mid)
            left = mid+1
        if left < right
            right = mid-1

        - keep doing this until left and right equal each other
        (while left < right)

        - should always end up in left and right being the same index
        - result can be nums[left] or nums[right]

        Time: O(logn)
        Space: O(1)
        '''
        curMin = float("inf")
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            curMin = min(curMin, nums[mid])

            if nums[mid] >= nums[right]:
                left = mid+1
            else:
                right = mid-1

        curMin = min(curMin, nums[left])
        return curMin
