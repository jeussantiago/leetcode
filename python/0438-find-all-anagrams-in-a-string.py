class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
        Sliding Window
        s = "zwscccbaaaebabacd", p = "abcc"
        Time: O(n)
        Space: O(n)
        '''
        p_counter = collections.Counter(p)
        s_counter = collections.Counter(s[:len(p)])

        res = [0] if s_counter == p_counter else []

        l, r = 0, len(p)
        while r < len(s):
            s_counter[s[r]] += 1
            s_counter[s[l]] -= 1

            if s_counter == p_counter:
                res.append(l + 1)

            r += 1
            l += 1

        return res
