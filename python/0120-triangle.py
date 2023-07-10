class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        '''
           2
          3 4
         6 5 7
        4 1 8 3

        - do this backwards
        - dp is the last row in triangle
        - for reverse rows so that you work backwards - start at the 2nd lowest row
            - for n in range(current_row num)
                add current [row][n] val + min(dp[n], dp[n+1])
                - save it into the dp at position n

        Time: O()
        Space: O()
        '''

        dp = triangle[-1]

        for row in range(len(triangle)-2, -1, -1):
            for n in range(row+1):
                dp[n] = triangle[row][n] + min(dp[n], dp[n+1])

        return dp[0]

        # TIME LIMIT EXCEEDING
        # triangle_height = len(triangle)

        # def helper(row, indx, total):
        #     if row >= triangle_height:
        #         nonlocal res
        #         #reached the bottom of triangle
        #         res = min(res, total)
        #         return

        #     total += triangle[row][indx]
        #     helper(row+1, indx, total)
        #     helper(row+1, indx+1, total)

        # res = float("inf")
        # helper(0, 0, 0)

        # return res
