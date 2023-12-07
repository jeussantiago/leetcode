class Solution:
    def largestOddNumber(self, num: str) -> str:
        '''
        could go forward but then you realise, the further you go,
        the bigger the number gets
        - so just get the first odd number

        Time: O(n)
        Space: O(1)
        '''
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                # odd number
                return num[:i+1]

        return ""
