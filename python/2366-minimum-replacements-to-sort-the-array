class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        '''
        work in reverse order
        - we can make a bigger number smaller but we cant make a smaller number bigger

        - now we can just check if the current value > the previous value(reverse order)
        if nums[i] > nums[i + 1]
            - if nums[i] divisible by nums[i + 1] => break into even parts
                => [9,3] => [3,3,3,3] (2 operations)
                length of breaking = num[i] / nums[i + 1]
            - if nums[i] not divisible by nums[i + 1] => break so that largest element is equivalent to (nums[i + 1]) and the smallest element (nums[i + 1] - 1)
                => [8,3] => [2,3,3,3]
                length of breaking = num[i] / nums[i + 1] + 1

            - we can add the number of operations to the results => length of breaking - 1
            
            - we don't need to add the entire broken down sequence of number, just the lowest number
                - update nums[i] with nums[i] // length of breaking
        
        Time: O(n)
        Space: O(1)
        '''

        res = 0
        N = len(nums)
        for i in range(N - 2, -1, -1):
            # sorted order already
            if nums[i] <= nums[i + 1]:
                continue

            if nums[i] % nums[i + 1] == 0:
                # evenly divisible
                breaking_length = nums[i] // nums[i + 1]
            else:
                # not evenly divisible
                breaking_length = nums[i] // nums[i + 1] + 1

            res += breaking_length - 1
            # update nums to be the sorted broken down min value
            nums[i] = nums[i] // breaking_length

        return res