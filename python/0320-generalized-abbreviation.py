class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        '''
        Time: O(n * 2^n)
        Space: O(n)
        '''
        N = len(word)
        res = []

        def dfs(start, path):
            if start >= N:
                res.append("".join(path))
                return

            # add the current letter
            dfs(start + 1, path + [word[start]])
            # add the converted count of letter to number
            if not path or path[-1].isalpha():
                for i in range(start, N):
                    dfs(i + 1, path + [str(i - start + 1)])

        dfs(0, [])
        return res
