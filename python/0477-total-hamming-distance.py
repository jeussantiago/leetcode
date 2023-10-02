class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        '''
        4 is  0100 
        14 is 1110
        2 is  0010

        - compare the first positions, all with each other [0, 1, 0]
            - the number of changes == number of 0s * number of 1s
            - this case [2 * 1  = 2 changes on the first position]
        - we then do this for all the positions

        - to count if the bit is 1 or 0, we can just have a pointer on the current bit 1 and move it by index in range of 32

        n is the length of nums
        Time: O(n)
            ; (32 * n) go through each number and with each numebr, you go through their bits one at a time, but each
            ; there is a max of 32 bits
        Space: O(1)
        '''
        res = 0
        for i in range(32):
            zeroes = ones = 0
            mask = 1 << i
            for num in nums:
                if mask & num:
                    ones += 1
                else:
                    zeroes += 1

            res += (zeroes * ones)

        return res
