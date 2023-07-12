class Solution:
    def partitionString(self, s: str) -> int:
        '''
        Time: O(n)
        Space: O(26) at most there are going to be 26 lowercase letters
             : O(1)

        '''

        res = 1
        appeared = set()
        for c in s:
            if c in appeared:
                # repeated char
                res += 1
                appeared = set()

            appeared.add(c)

        return res
