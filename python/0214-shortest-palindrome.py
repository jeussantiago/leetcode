class Solution:
    def shortestPalindrome(self, s: str) -> str:
        '''
        - check if the the substring is a palindrome
        - if it is a palindrome, update a tracker

        aacecaaa
        a +
        aa +
        aac x
        aace x
        aacec x
        aaceca x
        aacecaa +
        aacecaaa x

        - the tracker is on the position where you can add the reverse of everything after
        this to the beginning of the string

        Time: O(n)
        Space: O(1)
        '''
        ptr = 1
        for i in range(1, len(s)+1):
            if s[:i] == s[:i][::-1]:
                ptr = i

        return s[ptr:][::-1] + s
