class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        '''
        - didnt implement but an improvement on literal time would be to not append to stack if cnt == k, we would go immediatly to poppping

        - could also save a list instead of a tuple onto the stack so that i can manipulate the stack
            - if the top char is the same as current char, then increase the count of the top character
            - otherwise add to stack [char, 1]

        Time: O(n)
        Space: O(n)
        '''
        stack = []
        for char in s:
            cnt = 0
            if stack and stack[-1][0] == char:
                cnt = stack[-1][1]

            stack.append((char, cnt + 1))

            if stack[-1][1] == k:
                while stack and stack[-1][0] == char:
                    stack.pop()

        return "".join(char for char, _ in stack)
