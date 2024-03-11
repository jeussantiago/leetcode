class Solution:
    def customSortString(self, order: str, s: str) -> str:
        '''
        m is the length of order
        n is the length of s
        Time: O(n)
            ; (1) go through string 'order' but every character is unique so 
            ;   there are a max of 26 letters to got through
            ; (n) create a counter of string s to see how many times a letter appears
        Space: O(n)
            ; (n) string s counter
        '''

        cnt = collections.Counter(s)

        res = ""
        for char in order:
            if char in cnt:
                res += (char * cnt[char])
                cnt.pop(char)

        for char, freq in cnt.items():
            res += (char * freq)

        return res
