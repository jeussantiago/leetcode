class Solution:
    def calculate(self, s: str) -> int:
        '''
        - accounting multiple numbers bigger than one digit
        i.e. 14 =>
            curr = 1
            next digit is 4
            curr = (curr * 10 )+ curr_digit

        - deciding when to append the number, since some numbers are longer than others
            - a number ends when it gets to an operator (+ -)
            - so append the curr number to the stack when you see an operator

        - only add the number or the operator to the stack when you see a new operator
        10 - 4 + 3
        curr = 4 ; operator = "-"
        - currently on "+"
            - if the operator is "-"
                - add negative (curr_number) to the stack
            - if operator is "+"
                - add curr_number to the stack
        - ** we are only adding numbers to our stack, at the end we will only add everything
            - we have to deal with [-, *, /] before adding

        - if operator == "*"
            - stack.pop() * curr
            - then add this number to stack
            (consecutive multiplications will be fine since the number is on top of the stack)

        Time: O(n)
        Space: O(n)
        '''
        # s += "+0"
        stack, num, prev_operator = [], 0, "+"
        operators = {"+", "-", "*", "/"}

        for indx, c in enumerate(s):
            if c.isdigit():
                num = (num * 10) + int(c)

            if c in operators or indx == len(s)-1:
                if prev_operator == "+":
                    stack.append(num)
                elif prev_operator == "-":
                    stack.append(-num)
                elif prev_operator == "*":
                    stack[-1] *= num
                else:
                    stack[-1] = int(stack[-1] / num)

                prev_operator = c
                num = 0

        return sum(stack)
