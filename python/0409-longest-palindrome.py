class Solution:
    def longestPalindrome(self, s: str) -> int:
        pairs = set()
        res = 0
        for char in s:
            if char in pairs:
                pairs.remove(char)
                res += 2
            else:
                pairs.add(char)

        if len(pairs) > 0:
            res += 1

        return res
