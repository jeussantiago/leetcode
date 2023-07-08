class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        '''
            0 1 2 3 
        0   * 1 1 1
        1   1 0 X 0
        2   1 0 0 0

            0 1 2 3 
        0   * 1 1 1
        1   1 2 0 1
        2   1 3 3 4

            0 1 2 3 4 5 6 7
        0   * 1 X 0 0 0 0 0
        1   X
        2   0

        - similar question as 62. unique Paths
        - anywhere theres an obstacle, set that value to 0

        Time: O(m * n)
        Space: O(m * n)
        '''
        #obstacle in first position stops all movement
        if obstacleGrid[0][0] == 1: return 0

        #set the first row and col values
        N = len(obstacleGrid[0]) # column length
        M = len(obstacleGrid) # row length
        hasObstacle = False
        for i in range(1, N): 
            # give the position a 1 to signify the number of unique paths
            # if an obstacle is in the way, then every position after that is unreachable and should remain with 0 value (no paths lead there)
            if hasObstacle or obstacleGrid[0][i] == 1:
                #turn obstacle value to 0
                obstacleGrid[0][i] = 0
                hasObstacle = True
            else:
                obstacleGrid[0][i] = 1

        #range starting at 0 here rather than 1 like in the previous loop b/c we want to flip the first number
        hasObstacle = False
        for i in range(M): 
            if hasObstacle or obstacleGrid[i][0] == 1:
                obstacleGrid[i][0] = 0
                hasObstacle = True
            else:
                obstacleGrid[i][0] = 1

        #fill in the rest of the grid
        for row in range(1, M):
            for col in range(1, N):
                if obstacleGrid[row][col] != 1:
                    obstacleGrid[row][col] = obstacleGrid[row-1][col] + obstacleGrid[row][col-1]
                else:
                    #turn obstacle value to 0
                    obstacleGrid[row][col] = 0
        
        return obstacleGrid[-1][-1]





















