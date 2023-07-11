class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        # negative numbers/0 cannot be power of 2
        if n <= 0:
            return False
        # keep dividing the number while it can be divided by 2
        while n % 2 == 0:
            n = n / 2
        return n == 1
