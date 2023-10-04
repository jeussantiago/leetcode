class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        '''
        Time: O(n)
        Space: O(1)
        '''
        s = s.split("-")
        s = "".join(s).upper()
        res = ""
        for i in range(len(s)-1, -1, -k):
            res = "-" + s[max(i - k + 1, 0): i + 1] + res
        return res[1:]
