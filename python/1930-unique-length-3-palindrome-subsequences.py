class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        '''
        "b b c b a b a"
        - create a set out of the string
        set = {b,c,a}

        - then we can find the first and last instance of the characters
            - we can do that in place while creating the set but we can also use in built 
            functions like index() and rindex()
            (this will take more raw time but not more time complexity)

        - for each letter in the set, find the number of unique characters between the start
        and end points

        - add this number to the results

        Time: O(n)
            ; (n) creating the set
            ; (26) iterating through the letters set
            ; (n) find the first and last index of a char
            ; (n) iterating thorugh the first and last index to find the number of unique chars
            ; (n + 26(n + n)) => (n + 52n) => (n)
        Space: O(1)
            ; (26) set which contians the lower case letters
            ; (26) set to contain the in between lower case letters
        '''

        letters = set(s)
        res = 0
        for char in letters:
            start, end = s.index(char), s.rindex(char)
            unique_between = set()
            for i in range(start + 1, end):
                unique_between.add(s[i])

            res += len(unique_between)

        return res
