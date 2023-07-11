class Solution:
    def calculate(self, s: str) -> int:
        '''
        stack:

        "-(1-(4+5-2)-3)+(6+8)"

        - deal with longer numbers 
            - (num * 10) + curr_num
            14 => (0 * 10) + 1 => (1 * 10) + 4


        - if the opeartor is "+" or "-"
            - do the previous operation
            res += num * sign
            (update the sign)
            if operator == "+"
                sign = 1
            if operator == "-"
                sign = -1
            num = 0
        - if char is "("
            - add the res to the stack
            - add the sign to the stack
            (so that when we get out of the (), we can  apply the operator to the new number)
            - reset res (this is ok since we're adding the res to the stack for lookup later)
            - reset the sign to 1

        - if char is ")"
            - complete the rest of the expression before the ")"
                res += num * sign
            - popped the last sign, applying it to current number
                res = res * stack.pop() 
            - next item popped is the last digit, add this
                res = res + stack.pop()

            - reset num

        -(1-(4+5+2)-3)+(6+8)
        0 -1 
        res = 7 ; num = 2 ; sign = -1
        res = -6 ; num = 0 ; sign = -1

        - at the end there is still a number and a sign left to add so complete the operation

        Time: O(n)
        Space: O(n)
        '''

        res, num, sign, stack = 0, 0, 1, []
        for c in s:
            if c.isdigit():
                num = (num*10) + int(c)

            elif c in {"+", "-"}:
                res += (num * sign)
                sign = 1 if c == "+" else -1
                num = 0

            elif c == "(":
                stack.append(res)
                stack.append(sign)

                res = 0
                sign = 1

            elif c == ")":
                res += (num * sign)
                res *= stack.pop()
                res += stack.pop()

                num = 0

        return res + (num * sign)

        return 1
