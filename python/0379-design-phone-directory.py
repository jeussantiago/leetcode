class PhoneDirectory:
    '''
    Time: O(1)
    Space: O(k) ; where k is the number of valid released numbers

    '''

    def __init__(self, maxNumbers: int):
        self.maxNumbers = maxNumbers
        self.curr = 0
        self.released_nums_set = set()
        self.released_nums = []
        # self.nums = set(range(maxNumbers))

    def get(self) -> int:
        if self.released_nums:
            num = self.released_nums.pop()
            self.released_nums_set.remove(num)
            return num

        elif self.curr < self.maxNumbers:
            self.curr += 1
            return self.curr - 1

        else:
            return -1

        # if self.nums:
        #     return self.nums.pop()
        # return -1

    def check(self, number: int) -> bool:
        if number in self.released_nums_set or self.curr <= number < self.maxNumbers:
            return True
        return False
        # return number in self.nums

    def release(self, number: int) -> None:
        # don't want them to call release on a number that is already in the pool
        if number < self.curr and number not in self.released_nums_set:
            # valid non-present number. Release back into the pool
            self.released_nums_set.add(number)
            self.released_nums.append(number)

        # self.nums.add(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
