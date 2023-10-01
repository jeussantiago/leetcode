class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        Two Passes
        - take it word, put it in a list
        - reverse each word in a list
        - combine together

        Time: O(n)
        Space: O(n)

        One Pass
        - keep an empty variable as empty string
        - if char in s: then add to front of variable
        - if whitespace: then add current variable to results, and add a whitespace

        Time: O(n)
        Space: O(1)
        '''
        res = ""
        curr = ""
        for c in s:
            if c == " ":
                res += curr + " "
                curr = ""
            else:
                curr = c + curr

        res += curr

        return res
