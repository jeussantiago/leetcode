class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Time: O(m + n) where m is len of nums2 and n is the len of nums1
        # Space: O(m) mapping for nums2
        mapping = {num: ind for ind, num in enumerate(nums2)}
        return [mapping[num] for num in nums1]
