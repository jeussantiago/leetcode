class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        '''
        binary search - since the array is sorted

        Time: O(logn)
        Space: O(1)
        '''
        l, r = bisect_left(nums, target), bisect_right(nums, target)
        return (r - l) > (len(nums) // 2)


class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        '''
        Sorta brute to count every number

        Time: O(n)
        Space: O(1)
        '''
        majority = len(nums) // 2
        target_cnt = 0
        for num in nums:
            if num == target:
                target_cnt += 1

                if target_cnt > majority:
                    return True

        return False
