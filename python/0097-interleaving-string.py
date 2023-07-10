class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        '''
        s1 = "aabcc", s2 = "dbbca", 
        s3 = "aadbbcbcac"

             d b b c a  ''
         -------------------
         a | T F F F F | F 
         a | T F F F F | F  
         b | T T T T T | F
         c | F T T F T | F
         c | F F T T T | T
         -------------------
         ''| F F F F F   T        

        - as long as the character matches and theres a combination with the previous character and the other characters, the dp[i][j] = true
        Ex:
        s1 at pos: 3 and s2 and pos: 2
        - theres a combination with the s1 at pos 4 with the current characters of s2 and pos 2 that makes up the end portion of s3
        - thats why it is True
        - the dp[i][j] is not true because of s2 because s2[i][j+1] is false

        Time: O(n * m) 
        Space: O(n * m)
        '''

        N, M = len(s1), len(s2)
        if N + M != len(s3):
            return False
        dp = [[False] * (M+1) for i in range(N+1)]
        dp[N][M] = True

        for i in range(N, -1, -1):
            for j in range(M, -1, -1):
                if i < N and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < M and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True

        return dp[0][0]
