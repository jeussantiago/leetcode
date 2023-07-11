class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        hash map (does not fulfill the requirement of time(n) and space(1))

        Time: O(n)
        Space: O(n)
        '''
        cnt = collections.Counter(nums)
        for key, val in cnt.items():
            if val == 1:
                return key
