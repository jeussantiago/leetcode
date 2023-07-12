class Solution:
    def removeStars(self, s: str) -> str:
        # Stack Implementation
        # Time: O(n)
        # Space: O(n)
        res = []
        for c in s:
            if c == "*":
                # something
                res.pop()
            else:
                res.append(c)
        return "".join(res)
