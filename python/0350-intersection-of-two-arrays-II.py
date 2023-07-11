class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        Another solution: sort and 2 pointer
        Time: O(nlogn + mlogm)
        Space: O(n + m) biggest space usage would be from sorting in python
        '''
        nums1.sort()
        nums2.sort()
        i, j = 0, 0  # nums1 pointer, nums2 pointer
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1

        return res


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        Hashmap Solution:
        Time: O(n + m) ; creater counter dict then go through every element in nums2
        Space: O(min(n, m))
        '''
        count = collections.Counter(nums1)

        res = []
        for num in nums2:
            if num in count and count[num] > 0:
                res.append(num)
                count[num] -= 1

        return res
