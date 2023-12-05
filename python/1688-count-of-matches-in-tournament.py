class Solution:
    def numberOfMatches(self, n: int) -> int:
        '''
        Simulate
        Time: O(logn)
            ; cut in half
        Space: O(1)
        '''

        matches = 0
        while n != 1:
            if n % 2 == 0:
                matches += (n // 2)
                n //= 2
            else:
                matches += ((n - 1) // 2)
                n = ((n - 1) // 2) + 1

        return matches


class Solution:
    def numberOfMatches(self, n: int) -> int:
        '''
        Logic

        if there are n teams, there will always be n-1 matches played

        Time: O(1)
        Space: O(1)
        '''
        return n - 1
