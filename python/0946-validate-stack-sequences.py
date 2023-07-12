class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        '''
        Time: O(2n) ; worst case we add all the elements to the stack, then take all the elements out of the stack
            : O(n)
        Space: O(n)
        '''

        stack = []
        i = 0
        for num in pushed:
            stack.append(num)

            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1

        return not stack
