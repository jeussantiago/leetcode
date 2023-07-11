class Solution:
    def trailingZeroes(self, n: int) -> int:
        '''
        - every fifth factorial increases the number of trailingk 0's by +1
            0 - 4 = 0 trailing zeroes
            5 - 9 = 1 trailing zeroes 
            10 - 14 = 2 trailing zeroes
            15 - 19 = 3 trailing zeroes

        - num // 5 tells how many times 5 goes into n
        - it is also the same number as the number of trailing zeroes

        n = 30

        30//5 = 6 trailing zeroes
        - update teh current number
        n = 30//5

        6 // 5 = 1
        1 + 6 = 7
        n = 1

        1//5 = 0
        0 + 7 = 7
        n = 0

        Time: O(logn)
        Space: O(1)

        '''

        trailingCount = 0
        while n != 0:
            trailingCount += (n//5)
            n = n // 5

        return trailingCount
