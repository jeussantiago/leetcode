class Solution:
    def minOperations(self, nums: List[int]) -> int:
        '''
        - sort the array
        - at each position, we treat each number as the left most position in the continuous array
        - the right value = left_pos + len(nums) - 1
        - now we just need to find the numbers that aren't in the range [left, right]
        - since the nums is sorted, we can find the right value belongs in the nums using binary search
        - the amount of operations would (len(nums) - right_binary_insert_pos) + (left)

        - to account for duplicates, we can store the original length of the list 
            - then we can turn the nums into a set
            - this gets rid of the duplciates but keeps the idea of keeping the length of the original list

        Time: O(nlogn)
            ; (nlogn) sort
            ; (n) go through every number
            ;   (logn) binary search
        Space: O(n)
            ; (n) python sorting
        '''

        N = len(nums)
        res = N
        nums = sorted(set(nums))
        for left, leftVal in enumerate(nums):
            rightVal = leftVal + N - 1
            right = bisect_right(nums, rightVal)
            operations = N - right + left
            res = min(res, operations)

        return res
