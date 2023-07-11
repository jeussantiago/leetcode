class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        - if current token is a number
            - add to stack
        - if its a symbol
            - pop the last 2 items from stack
            - do operation (+,-,*,/)
            - add result to stack


        - solution is the last item in the stack

        Time: O(n)
        Space: O(1)
        '''
        stack = []
        for token in tokens:
            if token.isdigit() or (token.startswith("-") and token[1:].isdigit()):
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if token == "+":
                    res = num1 + num2
                elif token == "-":
                    res = num1 - num2
                elif token == "*":
                    res = num1 * num2
                else:
                    res = int(num1 / num2)

                stack.append(res)

        return stack.pop()
