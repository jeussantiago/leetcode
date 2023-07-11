class Solution:
    def reverseBits(self, n: int) -> int:
        '''

                  0b10100101000001111010011100
        n >> 5 =>      0b101001010000011110100
        n >> 6 =>       0b10100101000001111010
        n >> 7 =>        0b1010010100000111101
        n << 5 => 0b1010010100000111101001110000000
        n << 6 => 0b10100101000001111010011100000000
        n << 7 => 0b101001010000011110100111000000000
        ----------
        Reverse the bit
        0100  => 0010

        - can use (& 1 opeartor)
            - 0 & 1 = 0
            - 1 & 1 = 1
            (can perfectly copy)
        - puyt the bit in the right position

        n = 0100  res = ""
        - copy first bit in n (0)
        - slide n to the right so that it doesn't include (0 anymore)
        - add the copied bit to res
        - slide res to the left so that you leave space for the next bit (also implemented below)
        - OR
        - go to the position in the results and add the bit there using (| or) operator (implemented this version)
            - 0 | 1 = 1
            - 0 | 0 = 0
            - 1 | 1 = 1
        n =                   000000000000000000000000000011
        res =                 100000000000000000000000000000
        n_bit_shifted =       010000000000000000000000000000
        res (| or operator) = 110000000000000000000000000000

        n = 0100  res = 0000
        n =  010  res = 0000
        n =   01  res = 0010
        n =    0  res = 0010


        Time: O(32)
        Space: O(1)
        '''
        res = 0
        for i in range(32):
            # shift n to  the right and get the corresponding bit, which is now in the first position
            bit = (n >> i) & 1
            # keep everything in res the same, except for the bit pos that you want to replace
            res = res | (bit << (31 - i))
            # res = res << 1
            # res = res | bit

        return res
