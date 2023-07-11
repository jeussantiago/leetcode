class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        '''
        - work backwards
        - get the later letters before the beginning letters
        - current character = remainder
            - remainder = num % 26
            (if remainder is 0 however, that means it is 26, so just make it 26)
        - add character to start of string

        - update current number
        (num -1) // 26

        Time: O(logn)
        Space: O(1)
        '''

        res = ""
        while columnNumber > 0:
            rem = columnNumber % 26
            rem = rem if rem > 0 else 26
            c = chr(rem + 64)
            res = c + res

            columnNumber = (columnNumber - 1) // 26

        return res
