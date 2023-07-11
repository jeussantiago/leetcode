class Solution:
    def numSquares(self, n: int) -> int:
        '''
        Bottom up Approach:

        [1,4,9] ; target = 15

        [0
        1   1 = 1
        2   2 = 1 + 1
        3   3 = 1 + 1 + 1
        1   4 = 4 
        2   5 = 4 + 1
        3   6 = 4 + 1 + 1
        4   7 = 4 + 1 + 1 + 1
        2   8 = 4 + 4
        1   9 = 9 
        2   10 = 9 + 1
        3   11 = 9 + 1 + 1
        4   12 = 9 + 1 + 1 + 1
        2   13 = 9 + 4
        3   14 = 9 + 4 + 1
        4]   15 = 9 + 4 + 1 + 1

        dp[i] = min(dp[i-1] + 1, dp[i-current_square] + 1)

        - if the remaining taret value - current square iterating on < 0
            - then that means that there is no reason to go any further in testing the other squares, 
            since the amount of square needed is just going to get bigger and bigger
            - we want to find what equals the target

        T: O(n * sqrt(n)) go through each number in n, each n has to make sqrt(n) decisions. anymore 
        than sqrt(n) and it goes out of bounds
        S: O(n)
        '''
        squares = [i**2 for i in range(1, int(math.sqrt(n))+1)]

        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for num in range(1, n+1):
            for square in squares:
                if num - square < 0:
                    break
                dp[num] = min(dp[num], dp[num - square] + 1)

        return dp[-1]
