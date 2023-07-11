class Solution:
    def addDigits(self, num: int) -> int:

        s = str(num)
        while len(s) != 1:
            s = str(sum(int(i) for i in s))
        return int(s)
