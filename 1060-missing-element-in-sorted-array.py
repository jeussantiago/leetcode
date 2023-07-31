class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        '''
        [1,3,4,5,6,10,11] ; k = 2

        - get the lowest left position
        - get mid, 
            - offset the mid val by the starter val in the arr (arr[0])
            - then calculate the number of missing numbers by subtracting the mid_ind

        if missing_numbers < k:
            - move left pointer
            l = mid
        else missing_numbers >= k
            - move right pointer
            r = mid -1


        l = 0 ; r=6
        mid = 3
        5(arr[mid]) - 1 (arr[0]) = 4
        4 - 3(mid) = 1
        1 = missing_numbers
        1 (missing_numbers) < 3 (k):
            - move left pointer
            l = mid

        l = 3 ; r=6
        mid = 4
        6(arr[mid]) - 1 (arr[0]) = 5
        5 - 4(mid) = 1(missing_number)
        1(missing_number) < 3(k)
            l = mid

        l = 4 ; r=6
        mid=5 
        10(arr[mid]) - 1(arr[0]) = 9
        9 - 5(mid) = 4(missing_number)
        4(missing_number) !< 3(k)
            -move right pointer
            r = mid -1 

        l = 4 ; r=4

        - the kth missing number:
            - offset by first position
            - add k
            - add the left index
            1 + 2 + 4 = 7

        Time: O(logn)
        Space: O(1)
        '''

        l, r = 0, len(nums) - 1
        while l < r:
            mid = r - (r - l) // 2
            missing_numbers = nums[mid] - nums[0] - mid

            if missing_numbers < k:
                l = mid
            else:
                r = mid - 1

        return nums[0] + l + k
