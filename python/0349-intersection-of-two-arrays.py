class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # T: O(m + n) ; converting list to sets
        # S: O(n + m)
        nums = set(nums1)
        return [n for n in set(nums2) if n in nums]
