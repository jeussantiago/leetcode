class Solution:
    '''
    Time: O(2^n) at each character, there are 2 possible decisions to make, ignore the character or take it
                 the tree height is the size of the string
    Space: O(n) the recursion stack is the height of the tree and the solution set
    '''

    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.longest_string = -1
        self.res = set()

        self.dfs(s, 0, [], 0, 0)
        return list(self.res)

    '''
    parameters:
    s ; input string above
    curr_idx ; the current index of the string
    expr ; the the string we have created so far after iterating over the string
    open_paren_count ; open parenthesis count
    close_paren_count ; close parenthesis count
    '''

    def dfs(self, s, curr_idx, expr, open_paren_count, close_paren_count):
        # reached end of string
        if curr_idx >= len(s):
            # a valid parenthesis expression is only true if the number
            # of open parenthesis == number of close parenthesis
            if open_paren_count == close_paren_count:
                # if the current expression length is longer than the recorded longest string expression
                # we know those previous expressions are invalid and should be removed from
                # the solution set -> the current expression should be part of the solution set
                if len(expr) > self.longest_string:
                    print(self.res, "".join(expr))
                    self.longest_string = len(expr)
                    self.res = set()
                    self.res.add("".join(expr))
                elif len(expr) == self.longest_string:
                    self.res.add("".join(expr))
                # theres nothing to do to expressions that are not as long as the rest of the results in
                # the solution set

        # have not reached end of string
        else:
            curr_char = s[curr_idx]

            if curr_char == '(':
                # for (, we don't know whether we need to add it to the solution expression or not
                # so do both
                self.dfs(s, curr_idx + 1, expr, open_paren_count,
                         close_paren_count)  # ignored
                # added to expression
                self.dfs(s, curr_idx + 1, expr +
                         [curr_char], open_paren_count + 1, close_paren_count)
            elif curr_char == ')':
                # we can't take ) greedily like we did with closing parenthesis
                # this is b/c every closing parenthesis needs to have an open parenthesis before it
                self.dfs(s, curr_idx + 1, expr, open_paren_count,
                         close_paren_count)  # ignored
                if open_paren_count > close_paren_count:
                    # added to expression
                    self.dfs(s, curr_idx + 1, expr +
                             [curr_char], open_paren_count, close_paren_count + 1)
            else:
                # current character is a letter - we have to take all those
                self.dfs(s, curr_idx + 1, expr +
                         [curr_char], open_paren_count, close_paren_count)
