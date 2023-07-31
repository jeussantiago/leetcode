class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        '''
        - peak can't be on corners (0, n-1)

        - keep track of the highest peak index
        - get mid

        - update highest index

        - move left and right pointers
        - check the direction of slope, this is fine since mid can't be on the corners

        if arr[mid-1] < arr[mid] < arr[mid+1]
            - downward sloping
            - left_pointer = mid + 1
        else (arr[mid-1] > arr[mid] > arr[mid+1])
            - upward sloping
            - right_pointer = mid -1

        Time: O(logn)
        Space: O(1)
        '''
        highest_ind = None
        l, r = 0, len(arr) - 1

        while l <= r:
            mid = (l + r) // 2

            if not highest_ind or arr[mid] >= arr[highest_ind]:
                highest_ind = mid

            if mid == 0 or arr[mid-1] < arr[mid] < arr[mid+1]:
                l = mid + 1
            elif mid == len(arr) - 1:
                r = mid - 1
            else:
                r = mid - 1

        return highest_ind


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        '''
        Solution without keep track of highest index in another variable
        - keep the highest index in the array by adding it to the solution set
        - dont remove it from mid when move pointers

        Time: O(logn)
        Space: O(1)
        '''
        left, right = 0, len(arr) - 1

        while left < right:
            mid = left + (right - left) // 2

            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left
