class Solution:
    def canWinNim(self, n: int) -> bool:
        '''
        4 - lost
        5,6,7 - winnable
        8 - lost
        11,10,9 - winnable
        '''

        return n % 4 > 0
