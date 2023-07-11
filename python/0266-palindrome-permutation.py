class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        '''
        - every letter has to appear an even amount of tomes
        - 1 letter can appear an odd amount of times, but only 1 letter, no more, no less

        - create a counter dictionary

        s = "aab"
        {
            a: 2
            b: 1
        }

        - go through the values, count the number of odd numbers
        - if there are more than 1 odd numbers
            - return false

        Time: O(n)
        Space: O(n)
        '''
        counter = collections.Counter(s)

        oddCount = 0
        for val in counter.values():
            if val % 2:
                # odd
                oddCount += 1
                if oddCount > 1:
                    return False
        return True
