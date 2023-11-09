class Solution:
    def countHomogenous(self, s: str) -> int:
        '''
        Greedy

        - go consecutive, when the character changes, thats when you add the current count to the results

        abbcccaa
        1 3  6 3 

        zzzzz
            15

        Time: O(n)
        Space: O(1)
        '''
        MOD = 10**9 + 7
        res = 1
        consecutive_count = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                consecutive_count += 1
            else:
                consecutive_count = 1

            res += consecutive_count

        return res % MOD
