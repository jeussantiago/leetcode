class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        '''

        2 * 3 - 4 * 5

        - if the current character is a operator, split the string in half
            - left of operator
            - right of operator

        2 * (3 - 4 * 5)
            (3 - (4 * 5)) = (3 - 20) = -17
            (3 - 4) * 5 = (-1) * 5 = -5

        - each will return 1 number as its base case/lower levels
        - but then on the higher levels, we need to be able to do the parenthesis of different ones
        (put the results in a list and return the list)
        (lower levels will have 1 thing, higher levels will have more results)

        2 * -17 = -34
        2 * -5 = -10


        - some operations may be repeated so have a memoization dictionary
        (i.e. s = "3 - 4 * 5" => [-17, -5] ; possibel parenthesis solutions)


        '''

        memo = {}
        calculate = {
            "*": lambda x, y: x * y,
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y
        }
        operators = {"*", "+", "-"}

        def helper(s):
            if s in memo:
                return memo[s]
            if s.isdigit():
                return [int(s)]

            solutions = []
            for i, c in enumerate(s):
                if c in operators:
                    leftSolutions = helper(s[:i])
                    # don't include current index which is an operator
                    rightSolutions = helper(s[i+1:])
                    for l in leftSolutions:
                        for r in rightSolutions:
                            solutions.append(calculate[c](l, r))

            memo[s] = solutions
            return solutions

        return helper(expression)
