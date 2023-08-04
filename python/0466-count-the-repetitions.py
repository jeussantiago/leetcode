class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        '''
        s1 = "acb", n1 = 4, s2 = "ab", n2 = 2

        Time: O(s1.size * s2.size)
            ; (s1.size * s2.size) find out how many times s2 goes into s1
            ; (n1) for however many times s1 repeats(n1), increase the count and get to next pointer
        Space: O(s1.size * s2.size)
            ; dp max size
        '''
        # find out how many times s2 goes into s1 and the index
        dp = []
        s1_size, s2_size = len(s1),  len(s2)
        for i2 in range(s2_size):
            start, cnt = i2, 0
            for i1 in range(s1_size):
                if s1[i1] == s2[start]:
                    start += 1

                if start == s2_size:
                    start = 0
                    cnt += 1

            dp.append((start, cnt))

        res, ind = 0, 0
        for _ in range(n1):
            res += dp[ind][1]
            ind = dp[ind][0]  # next index to get count of

        return res // n2
