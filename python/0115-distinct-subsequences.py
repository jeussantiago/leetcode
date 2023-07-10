class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        '''
        - create t with the characters in s. characters have to be in order

        base cases:

        s = "a" ; t = ""
        - theres only 1 way to create t from s, don't grab any characters

        s = "" ; t = "a"
        - theres no way to create t from s

                    t

                      a b
                    0 1 2
                  ---------  
                0 | 1 0 0
        s     a 1 | 1 1 0
              b 2 | 1 1 1
              b 3 | 1 1 2

        - if the characters match, current_pos_value = [i-1][j-1]
        - at each row, just bring down the value of the previous row
            - at position (2,1) s=ab ; t=a
            - bring down the 1 from above
            - the character b != a, so we don't bring in the value from the diagonal
            - this keeps track of the number of times it takes to create a sequence with less characters



        Time: O(n * m)
        Space: O(n * m)
        '''
        S, T = len(s), len(t)
        # add extra layer to dp for base cases
        dp = [[0] * (T+1) for _ in range(S+1)]

        for i in range(S+1):
            dp[i][0] = 1

        for i in range(1, S+1):
            for j in range(1, T+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
        # print(s, t)
        # for d in dp:
        #     print(d)
        return dp[-1][-1]
