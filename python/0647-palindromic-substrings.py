class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        Time: O(n^2)
        Space: O(1)
        '''
        N = len(s)

        def countPalindrome(left, right):
            palindrome_cnt = 0
            # expand outwards until the substring isn't a palindrome anymore
            while left >= 0 and right < N and s[left] == s[right]:
                palindrome_cnt += 1
                left -= 1
                right += 1

            return palindrome_cnt

        res = 0
        for i in range(N):
            # odd length palindrome
            res += countPalindrome(i, i)
            # even length palindrom
            res += countPalindrome(i, i + 1)

        return res
