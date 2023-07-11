class RandomizedSet:
    '''
    List and Hashmap
    - list stores the vals
    - hashmap stores vals with coresponding list positions

    Time: O(1)
    Space: O(n)
    '''

    def __init__(self):
        self.nums = []
        self.exist = {}

    def insert(self, val: int) -> bool:
        if val in self.exist:
            return False

        self.nums.append(val)
        self.exist[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.exist:
            return False

        ind = self.exist[val]
        if ind != len(self.nums) - 1:
            # give the last element in the list, the val's current ind
            # - then swap their positions in the list
            self.exist[self.nums[-1]] = ind
            self.nums[ind], self.nums[-1] = self.nums[-1], self.nums[ind]

        # remove val from and list
        self.exist.pop(val)
        self.nums.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
