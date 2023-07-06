class Solution:
    def longestPalindrome(self, s: str) -> str:
        subStr = ""
        subStrLen = 0

        for i in range(len(s)):
            #odd palindrome substrings
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                #check if the palindrome is longer than the recorded one
                if (r - l + 1) > subStrLen:
                    #record new substr
                    subStr = s[l:r+1]
                    subStrLen = r - l + 1
                #update pointers
                l -= 1
                r += 1
            #even palindrome substrings
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                #check if the palindrome is longer than the recorded one
                if (r - l + 1) > subStrLen:
                    #record new substr
                    subStr = s[l:r+1]
                    subStrLen = r - l + 1
                #update pointers
                l -= 1
                r += 1
        
        return subStr
