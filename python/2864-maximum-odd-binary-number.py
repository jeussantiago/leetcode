class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        '''
        Time: O(n)
        Space: O(n)
        '''
        num_ones = s.count('1')
        return ('1' * (num_ones - 1)) + ('0' * (len(s) - num_ones)) + '1' 
        