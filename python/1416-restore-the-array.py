class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        '''
        Recursion top down
        m is the length of s
        Time: O(mlogk)
        Space: O(m)
        '''
        MOD = 10**9 + 7
        cache = {}

        def dfs(start):
            if start in cache:
                return cache[start]

            if start == len(s):
                return 1

            if s[start] == "0":
                return 0

            total = 0
            for end in range(start, len(s)):
                sub = s[start: end+1]
                if int(sub) > k:
                    break

                total += dfs(end + 1)

            cache[start] = total % MOD
            return cache[start]

        return dfs(0)


class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        '''
        TLE
        '''
        MOD = 10**9 + 7
        cache = collections.defaultdict(int)

        def dfs(i, sub):
            if i == len(s):
                return 1

            if (i, sub) in cache:
                return cache[(i, sub)]

            num = s[i]
            # print('here:', i,sub, num)
            if num != "0" and int(num) <= k:
                cache[(i, sub)] += dfs(i + 1, num)

            if int(sub + num) <= k:
                cache[(i, sub)] += dfs(i + 1, sub + num)
            # print(i, sub, '==>', cache[(i, sub)])
            cache[(i, sub)] %= MOD
            return cache[(i, sub)]

        return dfs(1, s[0])
