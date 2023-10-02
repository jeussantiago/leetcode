class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        '''
        length of side = sum(matchsticks) / 4
        if length_of_side != perimeter: then we can't create a square

        - reverse sort the matchsticks so that youre dealing with the biggest numbers firt

        - add the current stick length to one of the 4 possible sides if the sum is <= length_of_side
            - go to next index
        - since that would be a simulation, we need to remove the total from the index when trying for the other possible sides

        Time: O(4^n)
            ; (4^n) 4 possible options are each turn then the tree height is n
        Space: O(n)
            ; (n) recursion stack
        '''
        if len(matchsticks) < 4:
            return False

        length_of_side = sum(matchsticks) // 4
        # cant make square
        if length_of_side * 4 != sum(matchsticks):
            return False

        matchsticks.sort(reverse=True)
        N = len(matchsticks)
        sides = [0] * 4

        def dfs(ind):
            if ind == N:
                return all(side == length_of_side for side in sides)

            for i in range(4):
                if sides[i] + matchsticks[ind] <= length_of_side:
                    sides[i] += matchsticks[ind]
                    if dfs(ind + 1):
                        return True
                    sides[i] -= matchsticks[ind]

            return False

        return dfs(0)
