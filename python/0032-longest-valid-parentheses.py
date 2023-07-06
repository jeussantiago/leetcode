class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ''' 
        Stacks:
        - find last instance of a valid parenthesis => keep track of the indecies
        - add the indicies to the stack if character is '('
        - if character == ')' => remove/pop the last character from the stack (b/c it is '(' and that is part of the valid 
        character that you don't want to include)
        Example:
        - ((())) [-1,0,1,2]
        - ')' -> index: 3
        - pop from stack, which is 2, since the first valid character breakpoint is 
        before that (the index 2 is the point of '(' open parenthesis), we keep track of that breakpoint index
        - [-1,0,1] => 3-1 = 2 ; which is how many valid characters we currently have at this point
        - 1 signifies the start of the valid parenthesis substring
        
        Constraints:
        - len(s) between 0 - 3*10^4
        - all characters are either '(' or ')'
        ((())) [-1,0,1,2]

        Time: O(n)
        Space: O(n)
        '''
        res = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] =='(':
                stack.append(i)
            else:
                #keep track of last valid index
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    #valid parenthesis
                    res = max(res, i - stack[-1])
        return res
