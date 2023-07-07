class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        - go right -> down -> left -> up -> repeat
        [
            1 ,2 ,3 ,4 ,5 , 6
            7 ,8 ,9 ,10,11,12
            13,14,15,16,17,18
            19,20,21,22,23,24
            25,26,27,28,29,30
        ]

        left_boundary, right_boundary, top_boundary, bot_boundary = 0, len(matrix[0]), 0, len(matrix)

        while top_boundary <= bot_boundary or left_boundary <= right_boundary:

        row_cap, col_cap =  top_boundary, right_boundary
        go right:
            row = consistent
            col += 1
        row_cap, col_cap =  bot_boundary, right_boundary
        go down:
            row += 1
            col = consistent
        row_cap, col_cap =  bot_boundary, left_boundary
        go left:
            row = consistent
            col -= 1
        row_cap, col_cap =  top_boundary-1, left_boundary
        go up:
            row -= 1
            col = consistent

        left_boundary += 1
        right_boundary -= 1
        top_boundary += 1
        bot_boundary -= 1

        Time: O(m * n) where m is the len of the matrix and n is the len of individual arrays in matrix - go through each number only 1 time
        Space: O(1)
        '''
        res = []
        left_boundary, right_boundary, top_boundary, bot_boundary = 0, len(matrix[0]), 0, len(matrix)
        #go right -> down -> left -> up -> repeat
        while left_boundary < right_boundary and top_boundary < bot_boundary:
            #get numbers at the top - go right
            for i in range(left_boundary, right_boundary):
                res.append(matrix[top_boundary][i])
            #scaled the top - don't use that row anymore
            top_boundary += 1

            #get numbers at the right - go down
            for i in range(top_boundary, bot_boundary):
                res.append(matrix[i][right_boundary-1])
            #scaled the right - don't use that col anymore
            right_boundary -= 1

            #condition for the final traverse right (if matrix is horizontally long) and travers down (if matrix is vertically long)
            if top_boundary >= bot_boundary or left_boundary >= right_boundary:
                break

            #get numbers at the bottom - go left
            for i in range(right_boundary-1, left_boundary-1, -1):
                res.append(matrix[bot_boundary-1][i])
            #scaled the bottom - don't use that row anymore
            bot_boundary -= 1

            #get numbers at the left - go up
            for i in range(bot_boundary-1, top_boundary-1, -1):
                res.append(matrix[i][left_boundary])
            #scaled the left - don't use that col anymore
            left_boundary += 1

        return res

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''

        Another method:
        - get the top row
        - rotate the array conter clockwise (not including the top row)
        - repeat

        |1 2 3|      |6 9|      |8 7|      |4|  =>  |5|  =>  ||
        |4 5 6|  =>  |5 8|  =>  |5 4|  =>  |5|
        |7 8 9|      |4 7|

        Time: O(n + n^2) (maybe?) - good for small matrixes but not for very large ones
        Space: O(1)

        '''
        res = []
        while matrix:
            res.extend(list(matrix.pop(0)))
            matrix = list(zip(*matrix))[::-1]
        return res



















