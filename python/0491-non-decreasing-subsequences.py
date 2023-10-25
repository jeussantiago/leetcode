class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        '''
        - dfs -> add or don't add

        Time: O(2^n)
            ; 2 choices, add and don't add
            ; the height of each sequence would be n
        Space: O(2^n)
            ; hashset would be at most 2^n
            ; (n) recursion stack
        '''
        res = set()

        def dfs(ind, seq):
            if ind == len(nums):
                if len(seq) >= 2:
                    res.add(tuple(seq))
                return

            # don't add curr num
            dfs(ind + 1, seq)
            # add curr num
            if not seq or seq[-1] <= nums[ind]:
                dfs(ind + 1, seq + [nums[ind]])

        dfs(0, [])
        return res
