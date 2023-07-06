class Solution:
    def intToRoman(self, num: int) -> str:
        '''
        1) num between 1 and 3999

        Time: O(n)
        Space: O(1)

        Could of done hash table but didnt realise they were ordered until after
        '''
        symbols = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        roman = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        romanEquivalent = ''
        for i, val in enumerate(roman):
            symbolNumber = num // val
            if symbolNumber:
                num -= (val * symbolNumber)
                romanEquivalent += (symbols[i] * symbolNumber)

        return romanEquivalent
      