class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        '''
        - just follow the directions of the problem
        - use the last numebr to determine the next number to save space

        Time: O(n)
        Space: O(1)
        '''

        res = [pref[0]]
        for i in range(1, len(pref)):
            res.append(pref[i - 1] ^ pref[i])

        return res
