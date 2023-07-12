class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        '''
        mono decreasing stack

        - keep track of the min value to, this will act as the first number is 132
        - anything greater than the 2nd number in the stack ('3' in 132)
            - pop from the stack

        - you want the biggest number possible in the second position
        - this is why you pop if the current number is bigger since you can update the second number

        - if theres a new minimum
            - we don't need to do anything since we still need to wait for the second number
            - in the meantime, we can just throw it in the stack since its an invalid sequence and
            will be popped off from a value greater than itself

        [1,4,5,7,-1,8,9,6]

        [(1,4)] -> [] -> [(1,5)] -> [] -> [(1,7)] -> [(1,7),(1,-1)] -> min=-1 -> [(-1,8)] -> [(-1,9)]

        [3,5,0,3,4]

        [(3,5)] -> [(3,5), (3,0)] -> min=0 -> popped; 3 >= 0 [(3,5)] -> [(3,5),(0,3)] -> popped [(3,5)] ; 4 fits between

        [1,1,1,1,1]
        - stack would constantly be popped

        Time: O(n)
        Space: O(n)
        '''

        stack = []
        curMin = nums[0]
        for num in nums[1:]:
            while stack and num >= stack[-1][1]:
                stack.pop()

            # stack should have second value bigger than current number
            # just check if stack has value smaller than current number
            if stack and num > stack[-1][0]:
                return True

            stack.append((curMin, num))
            curMin = min(curMin, num)

        return False
