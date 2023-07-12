class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        '''
        Time: O(n)
        Space: O(n)
        '''

        stack = []
        for n in num:
            while stack and k > 0 and n < stack[-1]:
                stack.pop()
                k -= 1

            stack.append(n)

        stack = stack[:-k] if k else stack
        res = "".join(stack).lstrip("0")

        if not res:
            return "0"
        return res
