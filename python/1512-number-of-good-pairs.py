class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        '''
        Time: O(n)
        Space: O(n)
        '''
        freq = collections.defaultdict(int)
        res = 0
        for num in nums:
            freq[num] += 1
            if freq[num] >= 2:
                res += (freq[num] - 1)

        return res
