class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        - would do hash table but problem expects O(1) memory
        - check if the previous element is the same as the current element
            if same then delete element at index

        Time: O(n)
        Space: O(1)
        '''
        i = 1
        insertIndex = 1
        while i < len(nums):
            if nums[i-1] != nums[i]:
                nums[insertIndex] = nums[i]
                insertIndex += 1
            i += 1
        return insertIndex