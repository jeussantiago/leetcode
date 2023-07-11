class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''

        Time: O(n)
        Space: O(n)
        '''
        seen = {}
        for num in nums:
            if num in seen:
                return True
            seen[num] = True
        return False
