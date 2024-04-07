class Solution:
    def checkValidString(self, s: str) -> bool:
        '''
        Stack

        Time: O(n)
        Space: O(n)
        '''
        open_paren = []
        aster = []
        for i, char in enumerate(s):
            if char == '(':
                open_paren.append(i)
            elif char == '*':
                aster.append(i)
            else:
                # deal with corresponding closed brackets
                if open_paren:
                    open_paren.pop()
                elif aster:
                    # no open brackets, so take an astericks
                    aster.pop()
                else:
                    return False

        # might be leftover open parenthesis and asterisks
        while open_paren and aster:
            open_paren_ind = open_paren.pop()
            aster_ind = aster.pop()
            # open parenthesis needs to show before asterisks since
            # the asterisks is going to be a closed parenthesis
            if open_paren_ind > aster_ind:
                return False

        # false if theres still open parenthesis left
        # otherwise, if empty, true
        return not open_paren


class Solution:
    def checkValidString(self, s: str) -> bool:
        '''
        Time: O(n^2)
        Space: O(n^2)
        '''
        @cache
        def dfs(ind, parenthesis_cnt):
            if parenthesis_cnt < 0:
                return False

            if ind == len(s):
                # if all the parenthesis have a matching pair
                return parenthesis_cnt == 0

            char = s[ind]
            if char == '(':
                return dfs(ind + 1, parenthesis_cnt + 1)
            elif char == ')':
                return dfs(ind + 1, parenthesis_cnt - 1)
            else:
                return (
                    # treat asterisk as open parenthesis
                    dfs(ind + 1, parenthesis_cnt + 1)

                    # treat asterisk as a string
                    or dfs(ind + 1, parenthesis_cnt)

                    # treat asterisk as closed parenthesis
                    or dfs(ind + 1, parenthesis_cnt - 1)
                )

        return dfs(0, 0)
