class Solution:
    def minSteps(self, s: str, t: str) -> int:
        '''
        Time: O(n)
        Space: O(1)
            ; max itmes in counter is (26) because of 26 letters
        '''
        cnt = collections.Counter(s)
        res = 0
        for c in t:
            if cnt[c] > 0:
                cnt[c] -= 1
            else:
                res += 1

        return res
