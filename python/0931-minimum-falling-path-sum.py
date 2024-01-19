class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        '''
        Time: O(n)
        Space: O(1)
            ; no extra space used
        '''
        N = len(matrix)
        # get the lowest branch for each position
        for row in range(1, N):
            for col in range(N):
                # branches
                left_branch = matrix[row-1][col -
                                            1] if col >= 1 else float('inf')
                middle_branch = matrix[row-1][col]
                right_branch = matrix[row-1][col +
                                             1] if col < N - 1 else float('inf')

                matrix[row][col] += min(left_branch,
                                        middle_branch, right_branch)

        # check the last row for the min branch
        return min(matrix[N-1])
