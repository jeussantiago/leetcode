class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        - Brute Force
        - go through every number multiple times and use a lot of space

        Converging method:
        - get the multiplication of everything before a number
        - get the multiplication of everything after a number

        [1,2,3,4,5,6]
        num = 3
        before = 1 * 2
        after = 6 * 5 * 4
        - at num 3 position, we would put the product of those two before and after converging
        - it converging means that we aren't including the current number (in this case its 3) 
        - we do this for all the numbers

        [1,2,3,4]
        before: [1,1,2,6]
        after: [24,12,4,1]

        res: [24,12,8,6]


        Time: O(n)
        Space: O(1)
        '''
        N = len(nums)
        res = [1] * N
        # converging before
        total = 1
        for i in range(N):
            res[i] = total
            total *= nums[i]

        # converging after
        total = 1
        for i in range(N-1, -1, -1):
            res[i] *= total
            total *= nums[i]

        return res
