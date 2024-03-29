class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ''' 
        Two Pointers

        - have the right leading until you are k max elements away 
        from left pointer
        - move left pointer to the next max element position

        Time: O(n)
        Space: O(1)
        '''
        max_element = max(nums)
        left = 0
        res = 0
        for right in range(len(nums)):
            if nums[right] == max_element:
                k -= 1

            while k == 0:
                if nums[left] == max_element:
                    k += 1

                left += 1

            res += left

        return res
