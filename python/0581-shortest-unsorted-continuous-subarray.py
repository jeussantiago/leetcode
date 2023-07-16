class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        '''
        Stack:

        increasing_Stack (find the left pointer)
            - add values to the stack
            - while the current number is < the top value in the stack
                - pop the item from the stack
                - update the left pointer to be the minimum of whatever is popped and the curretn left_pointer

        decreasing_stack (find the right pointer)
            - add values to the stack
            - while the current number is > the top of stack
                - pop item from stack
                - update right pointer

        Time: O(n)
            ; (n) go through nums array
            ; (n) remove items from stack
            ; (2) do operation twice for left and right pointers
            => (2n)
        Space: O(n)
            ; (n) increasing stack
            ; (n) decresaing stack
        '''
        left = len(nums)
        inc_stack = []
        for i, num in enumerate(nums):
            while inc_stack and num < inc_stack[-1][0]:
                left = min(left, inc_stack.pop()[1])

            inc_stack.append((num, i))

        right = 0
        dec_stack = []
        for i in range(len(nums)-1, -1, -1):
            while dec_stack and nums[i] > dec_stack[-1][0]:
                right = max(right, dec_stack.pop()[1])

            dec_stack.append((nums[i], i))

        return max(right - left + 1, 0)
