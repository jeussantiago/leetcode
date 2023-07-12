class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ''' 
        Time: O(n)
        Space: O(1)
        '''

        res = 0
        height = 0
        for altitude_gain in gain:
            height += altitude_gain
            res = max(res, height)

        return res
