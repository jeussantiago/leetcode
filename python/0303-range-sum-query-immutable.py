class NumArray:
    '''
    Solution for the idea that sumRange is going to be called many, many times

    Originl list -  [1, 2, 3, 4, 5, 5, 6, 6]
    - sum of all numbers before index including itself
    Sum accumulation -  [1, 3, 6, 10, 15, 20, 26, 32]
    sum from left index to right index => right - (left - 1)
    - we do left - 1 since the accumulation includes the index when it adds all the numbers before hand

    '''

    def __init__(self, nums: List[int]):
        # T: O(n)
        # S: O(n)
        self.nums = list(itertools.accumulate(nums))
        print(self.nums)

    def sumRange(self, left: int, right: int) -> int:
        # T: O(1)
        # S: O(n)
        if left == 0:
            return self.nums[right]
        return self.nums[right] - self.nums[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
