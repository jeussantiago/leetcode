class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        '''
        Time: O(n)
        Space: O(5) ; vowels in set but we know th esize of that
             : O(1)
        '''

        vowels = set(['a', 'e', 'i', 'o', 'u'])

        vowel_cnt = 0
        for r in range(k):
            if s[r] in vowels:
                vowel_cnt += 1

        res = vowel_cnt
        l, r = 0, k
        while r < len(s):
            if s[r] in vowels:
                vowel_cnt += 1
            if s[l] in vowels:
                vowel_cnt -= 1

            res = max(res, vowel_cnt)
            r += 1
            l += 1

        return res
