class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        '''
        [{0}, {2}]
        [{-1,1}, {2, 4}]
        []

        Time: (n^2)
        Space: O(n^2)
        '''
        res = 0
        count = collections.defaultdict(int)
        for num1 in nums1:
            for num2 in nums2:
                count[num1 + num2] += 1

        for num3 in nums3:
            for num4 in nums4:
                res += count[-(num3 + num4)]

        return res
