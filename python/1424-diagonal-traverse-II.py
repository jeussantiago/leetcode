class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        '''
        Option 1:
        - get the rows and cols length
        - iterate diagonally
            - even if there is an empty space, go to the next diagonal space
            until you reach the row or col max

        - issue with this is dealing with the empty space 
        - worst case is:
        1 2 3 4 5 .... N .... 100
        101
        102
        103
        .
        .
        N
        .
        .
        10**7

        - so much dead space
        Time: O(n * n)

        Option 2: (Implemented here)
        - store each number value in a position in a 2d array
        - each number will corresponid to a position in the 2D array
        that corresponds to the diagonal order

        - in this way, you vist every position AND you don't visit
        the positions with empty space

        n is sum(nums[i].length)
        Time: O(n)
        Space: O(n)
        '''
        diag = []
        for start, row in enumerate(nums):
            ptr = start
            for num in row:
                if ptr == len(diag):
                    diag.append([])

                diag[ptr].append(num)
                ptr += 1

        res = []
        for row in diag:
            res.extend(row[::-1])

        return res


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        '''
        Option 3:

        BFS:

        - go DOWN then RIGHT
            - this will keep the correct order
            - only go down if the column position is the 0th position
        - this alleviates the issue of having to combine the list at the end

        Time: O(n)
        Space: O(sqrt(n))
            ; proportional to the largest diagonal
        '''

        diag = []
        q = collections.deque([(0, 0)])
        while q:
            row, col = q.pop()
            diag.append(nums[row][col])

            # add item below
            if col == 0 and row + 1 < len(nums):
                q.appendleft((row + 1, col))
            # add item to the right
            if col + 1 < len(nums[row]):
                q.appendleft((row, col + 1))

        return diag
