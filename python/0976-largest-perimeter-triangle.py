class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        '''
        to determine if 3 sides make a triangle
        a + b > c
        a + c > b
        b + c > a

        - if we sort, that means the biggest numbers come on the right
        - clearly anything + the biggest number is going to be bigger than the lower numbers
        - we just need to check if the lower numbers together is > than the biggest number

        - we go in reverse because the biggest triangle comes from the biggest numbers

        Time: O(nlogn)
        Space: O(n)
        '''

        nums.sort()
        for i in range(len(nums) - 3, -1, -1):
            if nums[i] + nums[i+1] > nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]

        return 0
