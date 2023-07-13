class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        '''
        n is the numbers of people
        m is the max number of accounts that a person has
        Time: O(n * m)
        Space: O(1)
        '''
        res = 0
        for account in accounts:
            res = max(res, sum(account))

        return res
