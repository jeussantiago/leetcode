class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        ["1","1","0","1","0"],
        ["1","1","1","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]

        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]

        - have visited index set
        - add index to visited set

        - if index is a "0"
            - continue
        - if current index is a "1" and not in visited
            - increase island count +1
        - else (index is a "1" and in visited)
            - treat it like normal 
        (the else doesnt' matter for the results)

        - check neighboring islands
            - if right is a "1" add it to visited
            - if bottom is a "1" add it to visited


        Recursion:
        - loop through all the indexes
        - if index not in visited and is a "1"
            new island => increase island counter by 1
            - find all the land pieces connected to it
        - otherwise, you can skip the space since it is either part of existing land or water

        Time: O(m * n)
        Space: O(m*n) grid and call stack but not saving other extra space bigger than O(1)
        '''

        visited = set()
        islands = 0
        M = len(grid)
        N = len(grid[0])

        def helper(row, col):
            if (
                row not in range(M) or
                col not in range(N) or
                grid[row][col] == "0" or
                (row, col) in visited
            ):
                return

            # go to neighboring is lands
            visited.add((row, col))
            directions = [(row, col+1), (row, col-1),
                          (row+1, col), (row-1, col)]
            for d_row, d_col in directions:
                helper(d_row, d_col)

        for row in range(M):
            for col in range(N):
                if grid[row][col] == "1" and (row, col) not in visited:
                    islands += 1
                    # get indexes of connecting islands
                    helper(row, col)

        return islands
