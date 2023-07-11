class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Time: O(n)
        # Space: O(n)

        seen = {}

        for i in range(len(nums)):
            if nums[i] in seen and (i - seen[nums[i]]) <= k:
                return True
            else:
                seen[nums[i]] = i
        return False
