class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        moving window on substrings
        Time: O(n)
        Space: O(n)
        '''

        # s = "fasdfghjkl"
        # s = "pwwkew"
        charSet = set()
        longestSub = 0
        #have a left pointer to keep track of the first position on the window/substring
        leftPointer = 0
        #right pointer to keep track of the last position of window/substring
        for rightPointer in range(len(s)):
            #slide the window's first/left position rightwards if the right position character is in the set
            while(s[rightPointer] in charSet):
                charSet.remove(s[leftPointer])
                leftPointer += 1
            #slide the window's last/right position to increase/add the next character
            charSet.add(s[rightPointer])
            #keep track of the longest substring
            if (longestSub < len(charSet)):
                longestSub = len(charSet)

        return longestSub
        