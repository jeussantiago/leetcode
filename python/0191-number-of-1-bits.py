class Solution:
    def hammingWeight(self, n: int) -> int:
        '''
        - length of binary is 32
        - get the first bit
            - if (bit | 0 is 1)
                - increase counter
        - shift n to the right
        '''

        res = 0
        for _ in range(32):
            bit = n & 1
            if bit:
                res += 1
            n = n >> 1

        return res
