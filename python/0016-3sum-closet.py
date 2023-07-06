class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        '''
        1) has exactly 1 solution
        2) array has atleast 3 numbers
        3) nums can be positive and negative
        4) target can be positive and negative

        sorting allows us to skip duplicate numbers so we can get through them faster
        [-3, -3, 0, 1, 2] -> skip duplicate numbers
        left and right pointer to come closer to target
        if less than target, move the left pointer rightwards by 1
        if more than target, move the right pointer leftwards by 1
        check the difference between 3 sum addition to target
        lowest difference is what you return
        '''
        nums.sort()
        closest_to_target = float('inf')
        closest_difference = float('inf')
        for i, num in enumerate(nums):
            l, r, = i+1, len(nums)-1
            while l < r:
                threeSum = num + nums[l] + nums[r]
                #check differences
                current_difference = abs(target - threeSum)
                if current_difference < closest_difference:
                    closest_difference = current_difference
                    closest_to_target = threeSum
                #update pointers
                if threeSum < target:
                    l += 1
                elif threeSum > target:
                    r -= 1
                else:
                    return target

        return closest_to_target

