class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        '''
        [0,0,0,1,1,1,0,0,0,1,1,0,0,1,1,0,1,1,0]
        [1,1,1,0]

        sec_last_zero_pos, last_zero_pos = initial(-1)
        last_zero_pos: simulates the 0 position that is going to be converted to a 1
        sec_last_zero_pos: the beginining position of the array of 1s (w/ last_zero_pos converted to a 1)

        Case: 1 at end
        [0,0,0,1]
            - solution: add a 0 to the end of the nums list or we can calculate it at the end

        if curr_num == 0
            - calculate the difference between current index position and sec_last_zero_pos 
            - update sec_last_zero_pos to be the value of last_zero_pos
            - update the new last_zero_pos to be current index position

        Time: O(n)
            ; Greedy
        Space: O(1)
        '''

        nums.append(0)
        res = 1  # since the list has to have a value in it, it can be 1 or 0, either way, min res should be 1
        sec_last_zero_pos = last_zero_pos = -1
        for i, num in enumerate(nums):
            if num == 0:
                res = max(res, i - sec_last_zero_pos - 1)
                sec_last_zero_pos = last_zero_pos
                last_zero_pos = i

        return res
