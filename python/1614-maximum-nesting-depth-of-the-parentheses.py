class Solution:
    def maxDepth(self, s: str) -> int:
        '''
        - count the number of parenthesis
        - can count with stack but can also just use a variable
        (hardest part about this problem is understanding
        the question and what it wants)

        Time: O(n)
        Space: O(1)
        '''

        res = 0
        parenthesis_cnt = 0
        for c in s:
            if c == '(':
                parenthesis_cnt += 1
                # could put this line at the end of the loop but we know we
                # only need to check when the count increases
                res = max(res, parenthesis_cnt)
            elif c == ')':
                parenthesis_cnt -= 1

        return res
