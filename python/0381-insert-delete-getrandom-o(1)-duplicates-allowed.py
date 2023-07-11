class RandomizedCollection:
    '''
    [1,2,3,4,1,4,3]
    {
        1: [0,4]
        2: [1]
        3: [2] 6
        4: [3,5]
    }
    last_num = 4

    remove 2:
    - pop the last ind in the array of key=2
    - we want to insert that ind into the last key=last_num_in_lst's dict
    - swap the positions in the list, last position, and the ind that was popped

    Time: O(1)
    Space: O(n)
    '''

    def __init__(self):
        self.lst = []
        self.dict = collections.defaultdict(set)

    def insert(self, val: int) -> bool:
        isPresent = False if len(self.dict[val]) > 0 else True
        self.lst.append(val)
        self.dict[val].add(len(self.lst) - 1)
        return isPresent

    def remove(self, val: int) -> bool:
        if len(self.dict[val]) == 0:
            return False

        # ind of val
        ind_val = self.dict[val].pop()
        # last number in array
        last_num = self.lst[-1]

        # swap the numbers in the array by giving the ind pos of val the value of last_num
        self.lst[ind_val] = last_num
        # add the new position/ind to the number set
        self.dict[last_num].add(ind_val)
        # remove the last position in the list from the set of the new number since the last_num still has the ind of its previous position stored
        # discard doesn't give error if the number doesnt exist, remove would give error
        self.dict[last_num].discard(len(self.lst) - 1)

        # take off the end of the list
        self.lst.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.lst)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
