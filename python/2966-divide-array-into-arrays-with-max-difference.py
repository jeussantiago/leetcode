class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        '''
        Time: O(nlogn)
        Space: O(n)
        '''

        nums.sort()
        res = []
        for i in range(0, len(nums), 3):
            # we don't need to check the other combinations in the
            # 3 width array since we are trying to find any 2 elements
            # that are not <= k. This means that we just need to check
            # the first and last element
            if nums[i + 2] - nums[i] > k:
                return []

            res.append([nums[i], nums[i + 1], nums[i + 2]])

        return res
