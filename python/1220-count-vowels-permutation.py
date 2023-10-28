class Solution:
    def countVowelPermutation(self, n: int) -> int:
        '''
        - each vowel has its own set of rules

        - dfs/backtracking
        - cache the position/current_n and the current string/last_vowel (since last vowel is the only thing we care about)

        - we have to start each search with each letter 'aeiou'

        Time: O(n)
            ; (5) start with each letter aeiou
            ; (n) n recursive calls for each vowel
            ; (1) each letter has their own set of rules they have to follow, at each step its a constant number
            ; of rules. Example: after 'a' is 'e' and after 'o' is 'i' or 'u'. The most rules is 4 for 'i' which makes it
            ; a constant
        Space: O(n)
            ; (n) recursive stack will be at most n size
            ; (5 * n) cache
        '''

        MOD = 10 ** 9 + 7

        @lru_cache
        def dfs(ind, vowel):
            total = 1
            if ind > 1:
                if vowel == 'a':
                    total = dfs(ind - 1, 'e') % MOD
                elif vowel == 'e':
                    total = (dfs(ind - 1, 'a') + dfs(ind - 1, 'i')) % MOD
                elif vowel == 'i':
                    total = (dfs(ind - 1, 'a') + dfs(ind - 1, 'e') +
                             dfs(ind - 1, 'o') + dfs(ind - 1, 'u')) % MOD
                elif vowel == 'o':
                    total = (dfs(ind - 1, 'i') + dfs(ind - 1, 'u')) % MOD
                else:
                    total = dfs(ind - 1, 'a') % MOD
            return total

        return sum(dfs(n, vowel) for vowel in 'aeiou') % MOD
