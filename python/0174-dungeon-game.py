class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        '''
        -  the knight needs to more health point than the minimum amount of health it needs to make 
        it to the bottom right
        - if need negative health, start at 0


        [-2,-3, 3]     [0,0,2]      [7,5,2] 
        [-5,-10,1]     [0,0,5]      [6,11,5]  
        [10,30,-5]     [1,1,6]      [1,1,6] 

        - do the problem bottom up (start from the princess position and figure out how 
        much health to get from the princess)
        - fill in the princess position and the last row and last col
        - pincress = max(1, 1-princess position)
        (if negative, we get a positive max -> if positive, we get a 1 max)
        - last row = max(1, pos[col+1] - pos[current col])
        - last col = max(1, pos[row+1] - pos[row](current pos) )

        fill in the middle:
        - max(1, min(right - self, bottom - self))


        dungeon = [[-3,5]]
        # output: 1  ; expected: 4 if at any point your number goes to 0, 
        you die, so you need enough to just survive al rooms
        [4, 1]

        Time: O(m*n)
        Space: O(m*n)

        '''
        M, N = len(dungeon), len(dungeon[0])  # rows, columns
        m, n = M-1, N-1

        health = [[1] * (N) for _ in range(M)]

        # fill in the princess
        health[m][n] = max(1, 1-dungeon[m][n])

        # fill in last row
        for col in range(n-1, -1, -1):
            health[m][col] = max(1, health[m][col+1] - dungeon[m][col])

        # fill in last col
        for row in range(m-1, -1, -1):
            health[row][n] = max(1, health[row+1][n] - dungeon[row][n])

        # fill in the middle part
        for row in range(m-1, -1, -1):
            for col in range(n-1, -1, -1):
                right_health = health[row][col+1] - dungeon[row][col]
                bottom_health = health[row+1][col] - dungeon[row][col]
                health[row][col] = max(1, min(right_health, bottom_health))

        # minimum required health is the first position
        return health[0][0]
