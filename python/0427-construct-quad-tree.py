"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        '''
        isLeaf:
            - every pos in the qadrants has the same value as every other pos in the quadrants
            - just check if everything matches the top left position

        val:
            - if everything is the same, the val is that number
            (or just top left number)
            - if they not everything is the same, then the val doesn't matter,
            - either way, just make th eevalue the top left position

        Recursion:
            - at each position
            - check if everything in the squares(all quadrants) are the same value

            - if everything same value:
                val = top left num
                isLeaf = True

            - if not the same:
                val = doesn't matter, make it top left
                isLeaf = False
                - recurse topLeft, topRight, botLeft, and botRight
                current_size = n
                - values to pass in:
                    - new size of square -> n//2
                    - new top left position (row, col)
                        topLeft: (row, col)
                        topRight: (row, col + new_size)
                        botLeft: (row + new_size, col)
                        botRight: (row + new_size, col + new_size)

        Time: O(n^2 * logn)
            ; (logn) continuosly split the size of the squares in half until size of squares==1
            ; (n^2) iterate/check each quadrant to see if all the numebres are the same
        Space: O(logn)
            ; (logn) recursion stack
        '''
        # size of the square, top left position (row, col)
        def dfs(size, row, col):
            # check if all the quadrants are the same value
            allSame = True
            for i in range(size):
                for j in range(size):
                    if grid[row][col] != grid[row + i][col + j]:
                        allSame = False
                        break

            # if same value - return leaf True
            if allSame:
                return Node(val=grid[row][col], isLeaf=True)

            # if not - recurse through each quadrant and create new node with leaf=False and quadrant children returns
            new_size = size // 2
            topLeft = dfs(new_size, row, col)
            topRight = dfs(new_size, row, col + new_size)
            botLeft = dfs(new_size, row + new_size, col)
            botRight = dfs(new_size, row + new_size, col + new_size)

            return Node(grid[row][col], False, topLeft, topRight, botLeft, botRight)

        return dfs(len(grid), 0, 0)
