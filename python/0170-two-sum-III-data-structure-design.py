class TwoSum:

    def __init__(self):
        # self.nums = []
        self.nums = {}

    def add(self, number: int) -> None:
        # self.nums.append(number)
        self.nums[number] = self.nums.get(number, 0) + 1

    '''
    - calculate the remaining difference ebtweent the target and current value
    - this remaining value is the number we're looking for when checking the
    later numbers
    - if any of those later numbers is one of those remaining values, then 
    there exist two numbers that add up to the value

    Time: O(n)
    Space: O(n)
    '''

    def find(self, value: int) -> bool:
        # seen = set()
        # for num in self.nums:
        #     if num in seen:
        #         return True
        #     difference = value - num
        #     seen.add(difference)
        # return False

        for num in self.nums:
            difference = value - num
            # print("t=",t)
            if difference in self.nums:
                if difference != num or self.nums[difference] > 1:
                    return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
