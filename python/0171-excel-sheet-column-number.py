class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        '''
        Time: O(n)
        Space: O(1)
        '''

        total = 0
        for expo, c in enumerate(columnTitle[::-1]):
            num = ord(c) - 64
            total += (num * (26**expo))

        return total
