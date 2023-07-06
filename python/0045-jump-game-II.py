class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        Greedy Solution: 
        [2,3,1,1,4,5] 
        [0,F,F,F,F]
        [0,1,1,F,F] - able to visit those index with 1 jump (update pointer)
        [0,1,1,2,2] - able to visit the 3rd index in 2 jumps but is greater than 1 so we keep the 1
        [0,1,1,2,2] - ind: 3 => 4th index gets there in 2 jumps but is greater than or equal than current 2 so we keep 2
        [0,1,1,2,2] - ind: 4 => 5th index gets there in 3 jumps but is greater than the current 2 so we keep 2
        minimum number of jumps to get to last index is 2

        0, 2, 2, 1
        1, 4, 2, 1
        2, 4, 4, 2
        3, 4, 4, 2
        4, 8, 8, 3

        - keep checking the farthest you can jump
        - if youve reached the fartest you can jump, you know you can increment a minimum jump counter
            - also updated what the new index of the maximum distance you can jump

        [2,3,3,3,4] 

        0, 2, 2, 1
        1, 4, 2, 1
        2, 5, 5, 2
        3, 6, 5, 2

        - check what the max distance you can jump is
        - set a pointer to where that maximum jump distance is
        - go through array
        - check current index and see what maximum jump you can take is (keep track of maximum distance at all times)
        - current index hasn't reached the previous max jumping distance (go to next ind)
        - check max jumping distance are current ind (its not greater than previous at 3)
        - finally have reached previous max jumping distance
            - get a new pointer to set for the max distance you can jump
            - increase a jump counter since that is the minimum amount to be able to jump that far
        - go next ind

        -* only really need to update the minimum jump counter if we've reached the maximum 
        distance we can go. we can confidently do that since the current index hasn't gotten to the
        end of the array and there is a solution to this problem. then we update the new max jumping distance
        so that when you do reach that new distance, we can first check if the index has reached the end,
        if not then we know we can keep searching and update the jumping counter

        Constraints:
        - the problem definitely has a solution to reach nums[n-1]
        
        Time: O(n)
        '''

        i, maxJump, lastMaxJumpingPosition, res = 0, 0, 0, 0
        while i < len(nums)-1:
            maxJump = max(maxJump, i + nums[i])
            #reached max jumping index
            if i == lastMaxJumpingPosition:
                #get a new max jumping distance
                lastMaxJumpingPosition = maxJump
                res += 1
            i += 1
        
        return res


