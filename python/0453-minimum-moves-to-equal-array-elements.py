class Solution:
    def minMoves(self, nums: List[int]) -> int:
        '''
        Time: O(nlogn)
        Space: O(1)
        '''
        nums.sort()
        moves = 0
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1] + moves

            nums[i] += moves
            moves += diff

        return moves
