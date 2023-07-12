class Solution:
    def canCross(self, stones: List[int]) -> bool:
        '''
        - you just keep jumping to the next one

        [3,5,6,8,12]
        - jump 2            or      jump 2
        - jump 1            or      not jump here
        - jump 2            or      jump 3
        - wouldn't make it  or      jump 4

        - keep searching jump to the next one if you can make it and then run dfs

        Time: O(n^2)
        Space: O(n)
        '''
        N = len(stones)
        cache = {}

        def dfs(ind, jump):
            if ind == N - 1:
                return True

            if (ind, jump) in cache:
                return False

            for j in range(ind + 1, N):
                if (jump - 1) <= (stones[j] - stones[ind]) <= (jump + 1):
                    if dfs(j, stones[j] - stones[ind]):
                        return True

            cache[(ind, jump)] = False
            return False

        return dfs(0, 0)
