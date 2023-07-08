class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        - go through each row, then each col
        - keep a set on the rows and cols that you have visited

        - after you've been through the row, replace the row with 0's
        - however, keep track of the columns that you need to change

        [
            [0,1,2,0],
            [3,4,5,2],
            [1,3,1,0]]

        [
            [0,0,0,0],
            [0,4,5,0],
            [0,0,0,0]]

        Time: O(m * n) size of matrix
        Space: O(m + n) size of matrix if you don't count the matrix itself, only the sets

        [1, 0, 2, 1]
        [3, 1, 0, 2]
        [1, 3, 1, 1]
        - keep track of the zero cols by storing the values in the first row
        - keep track of the zero rows by storing the values in the first col
        - every position in first row/col means that the entire row or col needs to be updated except the first (0,0) position
            - (0,0) position means it updates both row and col with has adverse effects to the updating as a whole
            - to combat this, have the (0,0) only reflect one update, now it only updates the cols
            - if its the first row, just keep track of needing to update the first row later in some boolean
        [1, 0, 0, 1]
        [0, 1, 0, 2]
        [1, 3, 1, 1]
        - now update everything except first row/col
        [1, 0, 0, 1]
        [0, 0, 0, 0]
        [1, 0, 0, 1]
        - if the (0,0) is 0, then that means the first column needs to be updated
        - if the boolean about the first row is True, then the first row needs to be updated as well
        [0, 0, 0, 0]
        [0, 0, 0, 0]
        [1, 0, 0, 1]

        Time: O(m * n) size of matrix
        Space: O(1) don't have other variables that save info into memory
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])
        rowZero = False

        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    if row == 0:
                        rowZero = True
                    else:
                        #keeps track of which row to turn 0
                        matrix[row][0] = 0 
                        #keeps track of which col to turn 0
                        matrix[0][col] = 0
        
        #change row and cols to 0's - skip the first row and col b/c if I turn the entire first row/col to zero then we can't figure out the actual values
        for row in range(1, ROWS):
            for col in range(1, COLS):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
        
        #update the first col
        if matrix[0][0] == 0:
            for row in range(1, ROWS):
                matrix[row][0] = 0

        #update the first row
        if rowZero:
            for col in range(COLS):
                matrix[0][col] = 0
















