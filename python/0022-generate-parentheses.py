class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        1) n is the number of correct parenthesis "()" is a string
        2) only able to add a closing parenthesis if the count of open parenthesis is greater than the count of closing parenthesis
        '''

        stack = []
        res = []

        def backtrack(openN = 0, closedN = 0):
            if openN == n and closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
            
        backtrack()
        return res