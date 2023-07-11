class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        '''
        - if the number is consecutive, then make a range out of  it
        - use a sliding window

        - left and right are going to be on the same idnex to start
        - keep moving the right pointer until r_value + 1 is not in the array
        - at this point, right should be on the last range

        - if left == right
            res.append(str(left))
        else
            f'{left}->{right}'

        Time: O(n)
        Space: O(n)
        '''
        numsSet = set(nums)
        res = []
        l, r = 0, 0
        while l < len(nums):
            while r < len(nums) and nums[r]+1 in numsSet:
                r += 1

            if l == r:
                res.append(str(nums[l]))
            else:
                res.append(f'{nums[l]}->{nums[r]}')

            l, r = r + 1, r + 1

        return res
