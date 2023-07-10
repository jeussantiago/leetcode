class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        '''
        |1 0 1 0 0| |1 0 1 0 0|
        |1 0 1 1 1| |2 0 2 1 1|
        |1 1 1 1 1| |3 1 3 2 2|
        |1 0 0 1 0| |4 0 0 3 0|

        - treat each row like a histogram (84. Largest Rectangle in Histogram)
        - for each row, we get the heights for each index
        |2 0 2 1 1|
        Stack:
        - if the number is increasing, add to stack
        - if the number is decreasing (current height < height in the last position in stack)
            - pop value from height
            - calculate the height that the value could have created



        Time: O(n * m)
        Space: O(n * m)
        '''
        # find the largest area in the row - treating it like a histogram
        def largestRectangleHistrogram(heights):
            stack, maxArea = [-1], 0
            heights.append(0)
            for i, h in enumerate(heights):
                while heights[stack[-1]] > h:
                    H = heights[stack.pop()]
                    maxArea = max(maxArea, (i - stack[-1] - 1) * H)
                stack.append(i)

            return maxArea

        # turn each row into a histogram
        # skip the first row
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1' and i > 0:
                    matrix[i][j] = int(matrix[i-1][j]) + 1
                else:
                    matrix[i][j] = int(matrix[i][j])

        # get the largest area for each row
        res = 0
        for row in matrix:
            res = max(res, largestRectangleHistrogram(row))

        return res
