class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        1) valid number between 1 - 3999
        2) 
        3) check next letter to see if it is bigger than previous, if it is then remove previous letter/number and insert new one
        
        Time: O(n)
        '''
        symbolRoman = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }

        num = 0
        previous_symbol = 'M'
        for symbol in s:
            if symbolRoman[symbol] > symbolRoman[previous_symbol]:
                num = (num - symbolRoman[previous_symbol]) + symbolRoman[previous_symbol+symbol]
            else:
                num = num + symbolRoman[symbol]
                
            previous_symbol = symbol

        return num