class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        2 pointer
        - whichever number in each array is lower
            - move that pointer up
        - then check if the numbers are the same

        Time: O(m + n)
        Space: O(1)
        '''

        N, M = len(nums1), len(nums2)
        ptr1, ptr2 = 0, 0  # ptr1 = nums1 pointer ; ptr2 = nums2 pointer
        while ptr1 < N and ptr2 < M:
            if nums1[ptr1] == nums2[ptr2]:
                return nums1[ptr1]

            if nums1[ptr1] < nums2[ptr2]:
                ptr1 += 1
            else:
                ptr2 += 1

        return -1
