class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        '''
        XOR(^) - if same, then 0        => 0, 0 and 1, 1 come to 0
               - if different, then 1   => 0, 1 and 1, 0 come to 1

        python inbuilt function to count number of bits after performing XOR
        Time: O(1)
        Space: O(1)
        '''
        return bin(x ^ y).count('1')


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        '''
        if don't want to use in built count function
        - shift the bits to the rightmost position
        - can compare the new number with 1
            new value & 1
            0101 & 0001
        Time: O(1)
        Space: O(1)
        '''
        xor = x ^ y
        res = 0
        while xor:
            if xor & 1:
                res += 1
            xor >>= 1
        return res
