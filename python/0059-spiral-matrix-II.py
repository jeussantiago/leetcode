class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        '''
        Similar to 54. Spiral Matrix in the way it traverses the matrix
        - create a board of size n x n

        fill top -> fill right -> fill bot -> fill left -> repeeat

        top_boundary, bot_boundary, left_boundary, right_boundary = 0, n, 0, n
        count = 1
        while top_boundary < left_boundary and left_boundary < right_boundary
            range(left_bondary, right_boundary)
                board[top_boundary][i] = count
                count += 1
            remove top row by increasing this boundary => top_boundary += 1

            -> repeate for other sides
        
        - if n is even, loop will need to go through all 4 sides
        - if n is odd, loop will need to only do the row once at the end

        [0, 0, 0, 0]
        [0, 0, 0, 0]
        [0, 0, 0, 0]
        [0, 0, 0, 0]

        Time: O(n * n) - go through each element one time
        Space: O(n * n) - board size

        '''
        board = [[0] * n for _ in range(n)]
        top_boundary, bot_boundary, left_boundary, right_boundary = 0, n, 0, n
        count = 1

        while top_boundary < bot_boundary:
            # top row
            for i in range(left_boundary, right_boundary):
                board[top_boundary][i] = count
                count += 1
            top_boundary += 1

            #early break for odd n matrix
            if top_boundary >= bot_boundary:
                break

            #right col
            for i in range(top_boundary, bot_boundary):
                board[i][right_boundary-1] = count
                count += 1
            right_boundary -= 1
            
            #bot row
            for i in range(right_boundary-1, left_boundary-1, -1):
                board[bot_boundary-1][i] = count
                count += 1
            bot_boundary -= 1

            #left col
            for i in range(bot_boundary-1, top_boundary-1, -1):
                board[i][left_boundary] = count
                count += 1
            left_boundary += 1

        return board










