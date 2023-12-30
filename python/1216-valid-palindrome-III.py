class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        '''
        Time: O(n^2)
        Space: O(n^2)
        '''

        cache = {}

        def isValid(l, r, k):
            if (l, r, k) in cache:
                return False

            if k < 0:
                return False

            # if manage to get to this point, then string is a plindrome
            if l >= r:
                return True

            # both characters are the same - move both pointers
            if s[l] == s[r]:
                if isValid(l + 1, r - 1, k):
                    return True
            # both characters are different - move left or right pointer
            # delete character
            else:
                if isValid(l + 1, r, k - 1) or isValid(l, r - 1, k - 1):
                    return True

            cache[(l, r, k)] = False
            return False

        return isValid(0, len(s) - 1, k)
