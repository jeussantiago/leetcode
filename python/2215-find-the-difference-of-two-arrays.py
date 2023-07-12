class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        '''
        Time: O(n + m)
                ; (n + m) convert each list to sets
                ; (n + m) iterate over each list and check if its not in the set
        Space: O(n + m) ; sets

        '''
        set1, set2 = set(nums1), set(nums2)
        l1, l2 = set(), set()

        for num in nums1:
            if num not in set2:
                l1.add(num)

        for num in nums2:
            if num not in set1:
                l2.add(num)

        return [list(l1), list(l2)]
