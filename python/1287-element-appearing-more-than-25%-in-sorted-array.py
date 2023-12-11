class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        '''
        since the array is sorted, we can check the n/4 position with the (i + n/4) position
        - the same numbers are next to each other and the arr[i] == arr[i + n/4]

        Time: O(n)
        Space: O(1)
        '''
        size = len(arr)//4
        for i in range(len(arr) - size):
            if arr[i] == arr[i + size]:
                return arr[i]

        return -1


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        '''
        Binary search (sorted array)

        since the array is sorted, we know at certain positions: 1/4th, 2/4th, 3/4th
        - these positions will contain the number that appears 1/4 times
        - we can go to these positions and check what the left most and right
        most index of the current number appears in
        arr = [1,2,2,6,6,6,6,7,10]
                   |   |   |
        1/4th = 2 => num 2
        2/4th = 4 => num 6
        3/4th = 6 => num 6
        - now we cann use binary search on these number appearances to find the 
        leftmost and the right most apearances of these numbers
        - if the appearance length is > n//4 then this number is our answer

        Time: O(logn)
        Space: O(1)
        '''
        n = len(arr)
        positions = [arr[n//4], arr[n//2], arr[3 * n // 4]]
        for num in positions:
            leftmost_ind = bisect_left(arr, num)
            rightmost_ind = bisect_right(arr, num) - 1
            print(leftmost_ind, rightmost_ind)
            if rightmost_ind - leftmost_ind + 1 > n//4:
                return num

        return -1
