class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        Greedy Solution: find a solution as fast as possible
        - we can work backwards
        [2,3,1,1,4] -> [4,1,1,3,2]
        - if we see that the position before the goal can reach the goal, then we can confidently say that if
        we reach that position, then we can reach the goal. the new array would kinda look like this:
        [2,3,1,1]
        [2,3,1]
        [2,3]
        [2]
        
        Time: O(n)
        Space: O(1)
        '''
        goal, i = len(nums)-1, len(nums)-2
        while i >= 0:
            #if the goal is within the number of jumps 
            if i + nums[i] >= goal:
                #update the new goal
                goal = i
            i -= 1
        #if the goal has been update to be 0 then that means the starting position can reach the goal
        return goal == 0
