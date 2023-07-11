class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        '''
        2 pointer solution

        Time: O(n)
        Space: O(n)
        '''
        counter = collections.defaultdict(int)
        res, distinct_cnt = 0, 0
        N = len(s)
        l = 0

        for r, c in enumerate(s):
            if counter[c] == 0:
                distinct_cnt += 1
            counter[c] += 1

            if distinct_cnt <= k:
                res = max(res, r - l + 1)

            while distinct_cnt > k:
                counter[s[l]] -= 1
                if counter[s[l]] == 0:
                    distinct_cnt -= 1
                l += 1

        return res
