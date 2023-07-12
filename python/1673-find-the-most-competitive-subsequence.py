class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        '''
        nums = [3,5,2,6] ; k=2 => res = [2,6]
        nums = [3,5,2,6,1] ; k=2 => res = [2,1]

        - we need to have len of results be k at the end

        Stack
        - if the current number is < the number at the top of the stack
            - keep popping the stack until the current number is >= the number at the top of the stack or until the stack is empty
            - we don't want to pop off too many numbers though, we need the size of the stack to be k at the end
            (-keep track of the current index of the amount of number allowed to be put into the current stack
             -compare it to the amount of remaining number left in the nums arr)

        - now the number at the top of the stack[-1] should be < the current num
            - add the number to the stack if there is enough space on the stack (len(stack) < k)

        EX:
        nums = [3,5,2,6,1] ; k=2
        -----------------------
        stack = [3,5] ; num = 2 ; ind = 2
        - 2 < 5 so we do want to pop off the last item in the stack
        - theres no more space in the stack but since 2 < 5, we can ateast replace that
        stack = [3] ; num = 2 ; ind = 2
        - 2 < 3 so we do want to pop off the last item in the stack
        - there is space to put an item onto the stack, we just have to figure out if we should pop 3 or not
        - we decide to pop 3 because the current number is < 3 and there are still remaining numbers in the arr
        that will fill the stack up to k length
        -----
        stack = [2] ; num = 6 ; ind = 3
        - nothing to pop since 6 > 2 ; just add 6 to the stack
        -----
        stack = [2,6] ; num = 1 ; ind = 4
        - 1 < 6 so we want to pop it off the stack
        - there is only 1 number remaining in the array so we can pop off the stack up to 1 times
        - we pop it off for that reason
        - we don't pop off 2 even though 1 < 2 because there are no more numbers in the array to fill the stack up to k length
        stack = [2,1] 

        Time: O(n)
        Space: O(n)
        '''
        N = len(nums)
        stack = []
        for i, num in enumerate(nums):
            # k - len(stack) <= N - i - 1 => (size of stack <= remaining numbers left in array)
            while stack and num < stack[-1] and k - len(stack) <= N - i - 1:
                stack.pop()

            if len(stack) < k:
                stack.append(num)

        return stack
