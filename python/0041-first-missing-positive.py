class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''
        - can't sort -> that would be time of O(nlogn)


        - if the number is less than zero or greater than the len(nums) 
            -> (we can't replace the number with a zero because 0 is the first index)
            -> (we can't replace the number with -1 because a negative shows that the number exist so it would create a contradiction)
            => only solution is to replace the number to len(nums)+1 because ti'd be out of bounds for the solution
        - all values in nums is positive now
        
        - if the num < len(nums) (within the solution bounds)
            - if nums[num-1] > 0
                - turn the number negative => nums[num-1] *= -1
        
        - now just look for any number greater than 0 and that is the index

        Time: O(n)
        Space: O(1)
        '''

        N = len(nums)
        for i in range(N):
            if nums[i] <= 0 or nums[i] > N:
                nums[i] = N + 1

        for i in range(N):
            num = abs(nums[i])
            #we don't want to go out of bounds by going to the index of the value 
            #we also want to check if that value has already been turned to negative (passes duplicate numbers)
            if num <= N: #and nums[num - 1] >= 0:
                nums[num - 1] *= -1

        for i in range(N):
            if nums[i] > 0:
                return i + 1
        return N+1























