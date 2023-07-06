class Solution:
    def reverse(self, x: int) -> int:
        num = ""
        if x < 0:
            num = int("-" + str(x)[:0:-1])
        else:
            num = int(str(x)[::-1])
        if num > 2**31 or num < -2**31:
            return 0
        return num