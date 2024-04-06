class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        '''
        Time: O(n)
        Space: O(n)
        '''
        # find which parenthesis are unnecessary
        non_valid_parentthesis_loc = set()
        open_parenthesis_loc = []
        for i, char in enumerate(s):
            if char == "(":
                open_parenthesis_loc.append(i)
            elif char == ")":
                if open_parenthesis_loc:
                    # there is a matching parenthesis
                    open_parenthesis_loc.pop()
                else:
                    # no matching parenthesis (stack empty)
                    non_valid_parentthesis_loc.add(i)

        non_valid_parentthesis_loc.update(open_parenthesis_loc)

        # get final string
        res = ""
        for i, char in enumerate(s):
            if i not in non_valid_parentthesis_loc:
                res += char

        return res
