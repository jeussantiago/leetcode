class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        '''
        [2, 3, 4, 7, 11]
        - compare to an array with no missing digits
        2 - 1 = 1 missing integer
        3 - 2 = 1 missing integer
        4 - 3 = 1 missing integer
        7 - 4 = 3 missing integers
        11 - 5 = 6 missing integers

        Binary search
        - mid = pivot point
        - if the number of missing integers at the pivot point < K
            - the kth missing integer is on the right side of the pivot point
            - move the left pointer
        - the number of missing integers at the pivot point > K
            - the kith missing integer is on the left side of the pivot point
            - move the right pointer

        left = 2
        - the kth missing value is the left (index + k)

        Time: O(logn)
        Space: O(1)
        '''

        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] - (mid + 1) < k:
                left = mid + 1
            else:
                right = mid - 1

        return left + k
