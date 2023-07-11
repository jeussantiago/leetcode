# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        '''
        [0,1,2,3,4]
        T: O(logn)
        S: O(1)
        '''
        l, r = 0, n-1
        while l < r:
            mid = (l + r) // 2
            version = mid + 1
            if isBadVersion(version):
                # don't do mid + 1 b/c mid is part of the solution, so can't not include it
                r = mid
            else:
                l = mid + 1
        return r+1
