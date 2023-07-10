class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        - start of a sequence means having no left neighbor/ having now number that is -1
        - being part of a sequence is having a left neighbor
        - make a set out of the list
        - check if a number exist in a set
        ** time complexity of checking if a number is in a list is -> O(n)
        ** time complexity of checking if a number is in a set/dict is -> Average: O(1) ; Worst: O(n)

        [100, 4, 200, 1, 3, 2]
        100 ->
        200 ->
        1 -> 2 -> 3 -> 4 -> None

        Time: O(n)
        Space: O(n)
        '''
        if not nums:
            return 0

        res = 0
        numSet = set(nums)

        for num in nums:
            if (num-1) not in numSet:
                # start of sequence
                length = 0
                while (num + length) in numSet:
                    length += 1

                res = max(res, length)

        return res
