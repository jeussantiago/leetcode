class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
        Stack

        - only keep track of the negative
        - add to stack
            - if the current is negative
            - while the top of stack is positive and abs(current negative number) is > top of stack
                - pop from

            - if the top of stack is negative
                - add current number to stack
            - elif top of stack is positive
                (this means that top of stack is > current Abs(negative number))
                - don't add curretn number to stack

        [-10,-5,8,-6,11,9,8,7,-10,-11]
        [-10,-5,8] -> [-10,-5,8] -> [-10,-5,8,11,9,8,7,-10] -> [-10,-5,8,11,-10] -> [-10,-5,8,11]
        -> [-10,-5,8,11,-11] -> [-10,-5,8]

        Time: O(n)
        Space: O(n)
        '''

        stack = []
        for num in asteroids:
            if num < 0:
                while stack and stack[-1] > 0 and abs(num) > stack[-1]:
                    stack.pop()

                if stack and stack[-1] == abs(num):
                    stack.pop()
                elif not stack or stack[-1] < 0:
                    stack.append(num)
            else:
                stack.append(num)

        return stack
