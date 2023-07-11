class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        '''

        Time: O(9^k)
        Space: O(9^k)
        '''
        end = n if n < 10 else 10
        res = []

        def helper(start, comb):
            if len(comb) == k:
                if sum(comb) == n:
                    res.append(comb)
                return

            for i in range(start, end):
                helper(i+1, comb + [i])

        helper(1, [])
        return res
