class Solution:
    def makeGood(self, s: str) -> str:
        '''
        [d,a,b,B,A,c,C,D]

        Stack

        Time: O(n)
        Space: O(n)
            ; since the max length of s is 100, then 
            ; we could say that time and space complexity 
            ; are O(1), but for this sake, it'll be O(n)
        '''
        stack = []
        for char in s:
            stack.append(char)

            while (
                len(stack) >= 2
                and abs(ord(stack[-1]) - ord(stack[-2])) == 32
            ):
                stack.pop()
                stack.pop()

        return "".join(stack)
