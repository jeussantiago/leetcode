class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        1) all combinations of digits given
        2) digits can be 0 - 4 numbers long
        3) individual digit can be in range of 2 - 9
        4) individual outputs are as long as the digits -> 234 => ['adg', 'adh', 'adi', 'aeg']
        
        recursion
        return output if len of current string creating is same as len of digits
        append current str to array
        go through current digit to char string
        call function - insert counter + 1 and current string as parameters
        start the function with base values such as 0 and ""

        '''

        digitToChar = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = []

        def comboPhone(i, currStr):
            if len(currStr) == len(digits):
                res.append(currStr)
                return
            for c in digitToChar[digits[i]]:
                comboPhone(i + 1, currStr + c)

        if digits:
            comboPhone(0, "")
            
        return res

