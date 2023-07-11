class Solution:
    def getMoneyAmount(self, n: int) -> int:
        '''
        n = 10

        low, high = 1, n
        - iterate through all possibilities of the guess => 1,2,3,4,5,6,7,8,9,10
            - set the initial low, high position to be 'inf'
            - but then we need to take the path of 'what if this guess wasn't the number and that number is either higher or lower'
            dfs(low, guess-1), dfs(guess+1, high)
            - if the guess is wrong, we need to add the current guess to the cost output

        if guess = 7
            dfs(low=1,high=guess-1),                                dfs(low=guess+1, high=10)
            guess = 3

            dfs(low=1, high=guess-1), dfs(low=guess+1, high=6)

        len is the distance between the left and right pointers
        dp[i][j] ; where i is the left start pointer 
                 ; where j is the right end pointer

        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        [0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0]       [0, 0, 1, 2, 4, 0, 0, 0, 0, 0, 0]       [0, 0, 1, 2, 4, 6, 8, 10, 12, 14, 16]
        [0, 0, 0, 2, 3, 0, 0, 0, 0, 0, 0]       [0, 0, 0, 2, 3, 6, 0, 0, 0, 0, 0]       [0, 0, 0, 2, 3, 6, 8, 10, 12, 14, 16]
        [0, 0, 0, 0, 3, 4, 0, 0, 0, 0, 0]       [0, 0, 0, 0, 3, 4, 8, 0, 0, 0, 0]       [0, 0, 0, 0, 3, 4, 8, 10, 12, 14, 16]
        [0, 0, 0, 0, 0, 4, 5, 0, 0, 0, 0]       [0, 0, 0, 0, 0, 4, 5, 10, 0, 0, 0]      [0, 0, 0, 0, 0, 4, 5, 10, 12, 14, 16]
        [0, 0, 0, 0, 0, 0, 5, 6, 0, 0, 0]       [0, 0, 0, 0, 0, 0, 5, 6, 12, 0, 0]      [0, 0, 0, 0, 0, 0, 5, 6, 12, 14, 16]
        [0, 0, 0, 0, 0, 0, 0, 6, 7, 0, 0]  ==>  [0, 0, 0, 0, 0, 0, 0, 6, 7, 14, 0] ==>  [0, 0, 0, 0, 0, 0, 0, 6, 7, 14, 16]
        [0, 0, 0, 0, 0, 0, 0, 0, 7, 8, 0]       [0, 0, 0, 0, 0, 0, 0, 0, 7, 8, 16]      [0, 0, 0, 0, 0, 0, 0, 0, 7, 8, 16]
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 9]       [0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 9]       [0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 9]
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9]       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9]       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9]
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ---------


        Time: O(n^2)
        Space: O(n^2)
        '''
        dp = [[0] * (n + 1) for _ in range(n + 2)]

        for dist in range(1, n + 1):
            for start in range(1, n - dist + 1):
                end = start + dist
                cur_min = float('inf')
                for guess in range(start, end + 1):
                    # if guess wrong, pay money equal to the guess value
                    cur_min = min(cur_min, max(
                        dp[start][guess-1], dp[guess+1][end]) + guess)
                dp[start][end] = cur_min

        return dp[1][n]
