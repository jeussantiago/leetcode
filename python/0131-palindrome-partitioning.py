class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
        "abccba"
        a b c c b a
        a b cc b a
        abccba

        "abccbas"
        a b c c b a s
        a b cc b a s

        "abas"
        a b a s
        aba s

                aab
            a   aa  aab
        a   ab  b   (X)
        b   (X) (O)   
        (O)
        [[a,a,b], [aa, b]]

        Time: O()
        Space: O()
        '''

        res = []

        def dfs(i, part):
            if i >= len(s):
                res.append(part)
                return

            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j+1):
                    dfs(j+1, part + [s[i:j+1]])

        dfs(0, [])
        return res

    def isPalindrome(self, s, i, j):
        return s[i:j] == s[i:j][::-1]
