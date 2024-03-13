class Solution:
    def pivotInteger(self, n: int) -> int:
        '''
        Two pointer

        Time: O(n)
            ; arguably O(1) cause theres a max of 1000 n
        Space: O(1)
        '''
        left_total = right_total = 0
        left, right = 1, n
        while left < right:
            if left_total < right_total:
                left_total += left
                left += 1
            else:
                right_total += right
                right -= 1

        if left_total == right_total:
            return left

        return -1
