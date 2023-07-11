class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''

        [4,1,2,1,2]

        4 ... 100
        1 ... 001
        2 ... 010
        1 ... 001
        2 ... 010

        XOR (^)
        1 ^ 1 = 0
        0 ^ 0 = 0
        1 ^ 0 = 1
        - same is 0
        - different is 1

        - XOR can be done in any order
        1 (001) ^ 2(010) = 011
        011 ^ 1(001) = 010
        010 ^ 4(100) = 110
        110 ^ 2(010) = 100

        - the bits cancel each other out. so repeating numbers get canceled out
        since you know theres 1 solution

        4(100)

        Time: O(n)
        Sapce: O(1)
        '''

        res = 0
        for n in nums:
            res = n ^ res
        return res
