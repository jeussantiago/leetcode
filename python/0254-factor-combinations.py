class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        # Time: O(nlogn)
        # Space: O(logn)

        res = []

        def helper(num, i, factors):
            # (start * start) to avoid duplicated
            while (i * i) <= num:
                if (num % i) == 0:
                    res.append(factors + [i] + [num // i])
                    helper(num // i, i, factors + [i])

                i += 1

        helper(n, 2, [])
        return res
