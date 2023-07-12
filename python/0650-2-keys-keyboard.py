class Solution:
    def minSteps(self, n: int) -> int:
        ''' 
        DP (when you se min and max of something, its probably a dp problem)
        '''
        self.res = float('inf')

        def dfs(screen, copied, operation_cnt):
            if len(screen) >= n:
                if len(screen) == n:
                    self.res = min(self.res, operation_cnt)
                return

            # copy
            if not copied or copied != screen:
                dfs(screen, screen, operation_cnt + 1)
            # past
            if copied:
                dfs(screen + copied, copied, operation_cnt + 1)

        dfs("A", None, 0)
        return self.res
