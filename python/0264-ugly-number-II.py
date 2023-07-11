class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # Time: O(n)
        # Space: O(n)

        dp = [1]
        i2, i3, i5 = 0, 0, 0
        for _ in range(1, n):
            a2, a3, a5 = dp[i2] * 2, dp[i3] * 3, dp[i5] * 5
            val = min(a2, a3, a5)
            dp.append(val)

            # increase the index of the multi that are the mins
            if a2 == val:
                i2 += 1

            if a3 == val:
                i3 += 1

            if a5 == val:
                i5 += 1

        return dp[-1]
