class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        '''
        - if the index is 0 or n-1
            - value in triangle is 1
        - else
            - [row-1][indx] + [row-1][ind-1]

        Time: O(n * n!)
        Space: O()
        '''

        pascals_triangle = [[1]]

        for row in range(1, numRows):
            current_row = []
            for n in range(row+1):
                if n == 0 or n == row:
                    current_row.append(1)
                else:
                    value = pascals_triangle[-1][n] + pascals_triangle[-1][n-1]
                    current_row.append(value)

            pascals_triangle.append(current_row)

        return pascals_triangle
