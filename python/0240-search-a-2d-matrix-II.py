class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row, col = len(matrix)-1, 0

        while row >= 0 and col < len(matrix[0]):
            num = matrix[row][col]

            if num > target:
                row -= 1
            elif num < target:
                col += 1
            else:
                return True

        return False
