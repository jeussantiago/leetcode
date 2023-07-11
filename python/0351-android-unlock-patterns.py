class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        '''
        Time: O(10^n)
        Space: O(n)

        '''
        skip = {
            (1, 3): 2,
            (1, 7): 4,
            (1, 9): 5,
            (2, 8): 5,
            (3, 1): 2,
            (3, 7): 5,
            (3, 9): 6,
            (4, 6): 5,
            (6, 4): 5,
            (7, 1): 4,
            (7, 3): 5,
            (7, 9): 8,
            (8, 2): 5,
            (9, 3): 6,
            (9, 1): 5,
            (9, 7): 8
        }

        def dfs(curr_num, count):
            ans = 1 if m <= count <= n else 0
            if count == n:
                return ans

            for num in range(1, 10):
                if (
                    num not in seen and (
                        (curr_num, num) not in skip or skip[(
                            curr_num, num)] in seen
                    )
                ):
                    seen.add(num)
                    ans += dfs(num, count + 1)
                    seen.remove(num)

            return ans

        res = 0
        for num in range(1, 10):
            seen = set([num])
            res += dfs(num, 1)

        return res
