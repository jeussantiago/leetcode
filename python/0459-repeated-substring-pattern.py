class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        '''
        - recreate the word at every position
        "abcabcabcabc"
        'a' * len(s) // 1
        'ab' * len(s) // 2
        'abc' * len(s) // 3

        - check if the create string == original string

        - we only need to go through half of the string since after that point, a pattern can't be created

        - we also only need to check on the indices that divide evenly into the length of s, 
            - trying to divide 5 in len(12) means that a pattern wont fit

        Time: O()
        Space: O(n)
            ; another string variable, same size as input s
        '''
        N = len(s)
        for i in range(1, (N // 2) + 1):
            if N % i == 0:
                pattern = s[:i] * (N // i)
                if pattern == s:
                    return True

        return False
