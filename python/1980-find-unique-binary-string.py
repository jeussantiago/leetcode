class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        '''
        Time: O(n^2)
            : (n^2) number of possibilities
        Space: O(n)
            ; (n) recursion stack
        '''
        nums_set = set(nums)
        N = len(nums)

        def dfs(curr):
            if len(curr) == N:
                if curr not in nums_set:
                    return curr
                else:
                    return ""

            res = dfs(curr + "0")
            if res:
                return res

            res = dfs(curr + "1")
            if res:
                return res

            return ""

        return dfs("")
