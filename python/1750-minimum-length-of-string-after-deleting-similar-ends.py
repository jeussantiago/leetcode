class Solution:
    def minimumLength(self, s: str) -> int:
        '''
        Time: O(n)
        Space: O(1)
        '''
        N = len(s)
        l, r = 0, N - 1

        while l < r:
            if s[l] != s[r]:
                break

            while l < r and s[l] == s[l + 1]:
                l += 1

            l += 1

            while r > l and s[r] == s[r - 1]:
                r -= 1

            r -= 1

        return max(0, r - l + 1)
