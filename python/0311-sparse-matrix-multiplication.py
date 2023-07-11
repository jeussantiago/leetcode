class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        '''
        A * B = C
        C_height = A_height
        C_width = B_width

        dot product = A row_0 * B col_0 | A row_0 * B col_1 | A row_0 * B col_2
                      A row_1 * B col_0 | A row_1 * B col_1 | A row_1 * B col_2
        (dot product not possible if the width_A == height_B ; this problem makes sure that it is possible)

        Time: O(n^3)
        Space: O(n^2)
        '''
        ROW1, COL1 = len(mat1), len(mat1[0])
        ROW2, COL2 = len(mat2), len(mat2[0])
        ROW3, COL3 = ROW1, COL2

        mat3 = []
        for row in range(ROW3):
            mat3.append([0] * COL3)

        for row in range(ROW3):
            for col in range(COL3):
                val = 0
                for i in range(COL1):
                    val += (mat1[row][i] * mat2[i][col])
                mat3[row][col] = val

        return mat3
