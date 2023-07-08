class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        Binary Search Approach
        16
        1,2,3,4....8,9,.....,16
        mid = 8
        8 * 8 > 16
        1,2,3,4....8
        mid = 4
        4 * 4 = 16 => return 4

        9
        1,2,3....9
        mid = 5
        5 * 5 > 9
        low = 1, high = 4
        mid = 2
        2 * 2 < 9
        res = 2
        low = 3, high = 4
        mid = 3
        3 * 3 = 9
        return 3

        Time: O(logn)
        Space: O(1)
        '''

        if x == 0 or x == 1: return x

        low = 1
        high = x
        while low <= high:
            mid = (low + high) // 2
            mid_sq = mid * mid
            if mid_sq == x:
                return mid
            elif mid_sq > x:
                high = mid - 1
            else:
                low = mid + 1
                res = mid
        return res
