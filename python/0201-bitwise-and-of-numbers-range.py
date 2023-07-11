class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        '''
        left: 9         00001001
        right: 12       00001100

        - problem calls to for the AND (&) operator between the left, right, and the range of numbers in between.
        But this is inconvenient for a really large range like [1, 2147483647]
        Solution:
        - right shift [>>] both left and right numbers until they're the same
            - keep track of how many times you right shifter

        - once they're the same number, take this value and shift it left, the same number of times
        as the tracked number

        [9]  00001001
        [12] 00001100

        0000100
        0000110
        shifted 1

        000010
        000011
        shifted 2

        [1] 00001
        [1] 00001
        shifted 3

        - now shift left

        answer = [8] 00001000


        Time: O(1)
        Space: O(1)
        '''

        count = 0
        while left != right:
            left = left >> 1
            right = right >> 1
            count += 1

        left = left << count

        return left
