class Solution:
    def __init__(self):
        self.res = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        [1,2,3]
        []
        [1] - [2,3], [1]
        [1,2] - [3], [1,2]
        [1,2,3] - [], [1,2,3]
        append to result
        [1,2] - [2,3], [1] (i goes to next index)
        [2], [1,3]
        [], [1,3,2]
        append to result - end of itration, go back a third time, increase i by 1
        i finishes loop - go back another time
        [1,3], [2]
        [1], [2,3]
        [], [2,3,1]
        [3], [2,1]
        [], [2,1,3]

        '''
        self.backtrack(nums, [])
        return self.res
    
    def backtrack(self, nums, path):
        if not nums:
            self.res.append(path)
        for i in range(len(nums)):
            #backtrack with the new nums not including the current number, path adds the current number
            self.backtrack(nums=nums[:i]+nums[i+1:], path=path+[nums[i]])

        