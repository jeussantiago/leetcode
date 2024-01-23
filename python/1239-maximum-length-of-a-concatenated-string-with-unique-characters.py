class Solution:
    def maxLength(self, arr: List[str]) -> int:
        '''
        Time: O(2^n)
            ; 2 decisions to take the next string or skip
            ; (n) have to go through every string in array
        Space: O(n)
            ; (n) recurions stack
        '''

        def dfs(i, s):
            if len(s) != len(set(s)):
                return 0

            res = len(s)
            for j in range(i, len(arr)):
                res = max(res, dfs(j + 1, s + arr[j]))

            return res

        return dfs(0, "")
