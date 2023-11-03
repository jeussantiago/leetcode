class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        '''
        Time: O(n)
        Space: O(1)
        '''

        curr_count = 1
        res = []
        for num in target:
            while curr_count < num:
                res.append('Push')
                res.append('Pop')
                curr_count += 1

            res.append('Push')
            curr_count += 1

        return res
