class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        '''
        find the continuous strings
        s = "tdezab"
        - number of possibilites = (len + 1) * len // 2

        t = 1 ; de = 2 ; zab = 3
          = 1 ;    = 3 ;     = 6
        ['t', 'd', 'e', 'de' ,"z", "a", "b", "za", "ab","zab"]

        "abcabcde"
        [1,2,3,1,2,3,4,5]
        [1,2,3] => (repeats with second 'abc) => [1,2,3,4] => [1,2,3,4,5]

        Time: O(n)
        Space: O(1)
            ; not counting the space used for the results
        '''
        res = 0
        dp = [1] * len(s)
        counter = [0] * 26

        # fill the dp with the consecutive counts
        for i in range(1, len(s)):
            if (s[i-1] == 'z' and s[i] == 'a') or ord(s[i]) - ord(s[i-1]) == 1:
                dp[i] += dp[i-1]
        # add the number of uniques
        for i in range(len(dp)):
            ind = ord(s[i]) - ord('a')
            # increase the unique count based on the the number of times it shows
            res += max(dp[i] - counter[ind], 0)
            # keep track of the repeated values/substrings which is the biggest number
            counter[ind] = max(counter[ind], dp[i])

        return res
