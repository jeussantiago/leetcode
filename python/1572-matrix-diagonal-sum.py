class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        '''
        Time: O(n) ; where n is the len of the matrix
        Space: O(1)
        '''
        N, M = len(mat), len(mat[0])
        res = 0
        # visited = set()
        for i in range(N):
            # negative diagonal
            res += mat[i][i]
            # positive diagonal
            if N - i - 1 != i:
                res += mat[N - i - 1][i]

        return res
