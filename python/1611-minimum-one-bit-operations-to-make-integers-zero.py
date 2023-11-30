class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        '''
        ** Just pray you don't get this problem in an interview

        n = 3
        1000
        1001
        1011
        1010
        1110
        1111
        1101
        1100
        0100
        - we finally removed the most significant digit
        - to remove the next significant digit, we just need to go backwards, 
            since it was alreayd removed at an earlier point in time
        - similuate recursion:
            - we can remove the last digit by doing the XOR operation
            (2**k) ^ n == (2**k) XOR n

        Time: O(logn)
        Space: O(1)
        '''
        if n == 0:
            return 0

        k = 0
        while 2**k <= n:
            k += 1
        # k is over, so we need to decrease it
        k -= 1

        return 2**(k + 1) - 1 - self.minimumOneBitOperations(2**k ^ n)
