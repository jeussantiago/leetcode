
class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        "01" = 0 b/c starts with 0 and 0 is not in mapping => +0
        "22" = if num between 10 and 26, that means theres 2 ways to decode it (2 and 2 or 22) => +2
        "29" = if number over 26, that means theres 1 way to decode it (2 and 9) => +1
        "10" = 10 and 20 are the only exception for rule #2, since you can't decode a 0, theres only 1 way to decode this (as 10 alone) => +1
        "90" = if num over 26 and ends in a zero, then theres no way to decode (res=0) => +0
        "3" = as long as this num isn't 0, then theres only one way to decode this number, by itself (3) => +1

        11106
        -----------------------
        {5: 1}
        6 {5: 1, 4: 1}
        0 {5: 1, 4: 1, 3: 0}
        1 {5: 1, 4: 1, 3: 0, 2: 1}
        1 {5: 1, 4: 1, 3: 0, 2: 1, 1: 1}
        1 {5: 1, 4: 1, 3: 0, 2: 1, 1: 1, 0: 2}

        '''
        dp = [0] * (len(s)+1)
        dp[len(s)] = 1
        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            # if number is double digit 10-26
            if (
                i + 1 < len(s) and (
                    (s[i] == '1') or
                    (s[i] == '2' and s[i+1] in "0123456")
                )
            ):
                dp[i] += dp[i + 2]

        return dp[0]


class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        - if substring is not in key, then theres no reason to continue
        - base case:
            - reason we have ind > len(s) is b/c ind+2 is outputting the same answer as ind+1 at the very end
            (11106 ind+1 and ind+2 use '6' at the end so itll both be true, however we don't want both to be true)

        Time: O()
        Space: O()
        '''
        key = [str(i) for i in range(1, 27)]
        res = 0

        def dfs(ind):
            if ind == len(s):
                nonlocal res
                res += 1
                return
            sub_one = s[ind:ind+1]
            if sub_one not in key:
                return
            dfs(ind+1)

            sub_two = s[ind:ind+2]
            if sub_two not in key:
                return
            dfs(ind+2)

        dfs(0)
        return res
