class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])  # row, col
        res = float('-inf')
        max_sum = float('-inf')

        # iterate through all columns, mimicking the left side of the box
        for left in range(n):
            # prefix sum of items in each row
            temp = [0] * m

            # iterate through the rest of the columns mimicking the right side of the box
            for right in range(left, n):

                # at the current col, add the element val to the prefix sum
                for i in range(m):
                    temp[i] += matrix[i][right]

                # calculate teh current cumulative sum for teh prefix sum so far
                # where the subarray for the cum_sum is, where the top and bottom boundaries are for the box
                # Kadane's algorithm to find max sum of subarray <= k
                cum_sum = 0
                cum_sum_set = [0]

                for t in temp:
                    cum_sum += t
                    it = bisect_left(cum_sum_set, cum_sum - k)
                    if it != len(cum_sum_set):
                        max_sum = max(max_sum, cum_sum - cum_sum_set[it])
                    bisect.insort(cum_sum_set, cum_sum)

        return max_sum
