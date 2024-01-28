class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        '''
        n in the number of rows
        m is the number of columns
        Time: O(n^2 * m)
        Space: O(m)
            ; not creating new matrix for prefix sums
            ; (m) hash table is the size of the number of COLS
        '''
        ROWS, COLS = len(matrix), len(matrix[0])
        # calculate prefix sum -> 2D version is add the top,
        # left, and current value, and subtract the top-left diagonal
        for row in range(ROWS):
            for col in range(COLS):
                matrix[row][col] = (
                    matrix[row][col]
                    + (matrix[row - 1][col] if row >= 1 else 0)
                    + (matrix[row][col - 1] if col >= 1 else 0)
                    - (matrix[row - 1][col - 1]
                       if row >= 1 and col >= 1 else 0)
                )

        res = 0
        # treat 2D array like a 1D array
        # have two row pointers, a leading row pointer and a trailing row pointer
        for row1 in range(ROWS):
            for row2 in range(row1, ROWS):

                matrix_sums = collections.defaultdict(int)
                # empty matrix sum = 0
                matrix_sums[0] = 1

                for col in range(COLS):
                    # calculate the submatrix sum
                    submatrix_sum = (
                        matrix[row2][col]
                        - (matrix[row1 - 1][col] if row1 >= 1 else 0)
                    )
                    # look for the raimander of the submatrix total and the target
                    # in the dict, this value represents the number we're looking for
                    # and the count of it means that we can add it to the results
                    res += matrix_sums[submatrix_sum - target]
                    # increase the count of submatrix total
                    matrix_sums[submatrix_sum] += 1

        return res
