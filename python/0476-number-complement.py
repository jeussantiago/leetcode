class Solution:
    def findComplement(self, num: int) -> int:
        '''
        - compare every position with XOR 1
            XOR = if its the same, will turn to 0, if its different will turn to 1

        Time: O(1)
            ; no more than 32 positions
        Sapce: O(1)
        '''

        compareBit = 1
        todo = num
        while todo:
            num = num ^ compareBit  # XOR
            compareBit = compareBit << 1

            todo = todo >> 1

        return num
