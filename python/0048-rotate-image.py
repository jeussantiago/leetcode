class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        [
            [1,2],
            [3,4]
        ]
        [
            [3,1],
            [4,2]
        ]
        - column becomes row (
            1: 0,0 -> 0,1 ; 
            3: 1,0 -> 0,0 ; 
            2: 0,1 -> 1,0 ; 
            4: 1,1 -> 1,0)
        

        [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
        [
            [7,4,1],
            [8,5,2],
            [9,6,3]
        ]
        - (
            1: 0,0 -> 0,2
            2: 0,1 -> 1,2
            3: 0,2 -> 2,2
        )

        [
            [5,1,9,11],
            [2,4,8,10],
            [13,3,6,7],
            [15,14,12,16]
        ]
        [
            [15,13,2,5],
            [14,3,4,1],
            [12,6,8,9],
            [16,7,10,11]
        ]
        - (
            4: 1,1 -> 1,2
            8: 1,2 -> 2,2
            3: 2,1 -> 1,1
            6: 2,2 -> 2,1
        )

        - left side to top row : matrix[row-i][col] => matrix[row][col+i]
        - top row to right side : matrix[row][col+i] => matrix[row+i][col]
        - right side to bottom row: matrix[row+i][col] => matrix[row][col-i]
        - bottom row to left side: matrix[row][col-i] => matrix[row-i][col]
        - can't have rows and cols as input values because sometimes we need the rows to count down but other times we need it to count up
        top, bottom = row, col
        i is so that we know which square we are on
        - working from outside in (working in quadrants/halfway point )

        Time: O(n^2)
        """
        l, r = 0, len(matrix)-1
        while l < r:
            for i in range(r-l):
                top, bot = l, r
                #top row
                topRow = matrix[top][top+i]
                #left side to top row
                matrix[top][top+i] = matrix[bot-i][top]
                #bottom row to left side
                matrix[bot-i][top] = matrix[bot][bot-i]
                #right side to bottom row 
                matrix[bot][bot-i] = matrix[top+i][bot]
                #top row to right side
                matrix[top+i][bot] = topRow
            #go to next inside square
            r -= 1
            l += 1
























