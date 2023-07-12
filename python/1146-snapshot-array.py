class SnapshotArray:
    '''
    -  need to find a way to reduce the amount of space usage
    - one approach is to create a 2D array of length 5 * 10^9 or size length and add a new row when snap is called
    - this would allow for O(1) approaches in all cases but the space usage would be much bigger

    Space Optimization:
    - have a list or dictionary of size length initailly
    - at each position keep a list
    - each list value will be [curr_index_val, curr_snap_id]
        - if the curr_snap_id already exist (the last id == current_id,  update the curr_val)

    - when we need to get a value from a specific id, we can just do binary search

    '''
    # Time: O(n)

    def __init__(self, length: int):
        self.id = 0
        self.history = collections.defaultdict(list)
        for i in range(length):
            self.history[i].append([self.id, 0])

    # Time: O(1)
    def set(self, index: int, val: int) -> None:
        if self.history[index][-1][0] == self.id:
            # update the current val
            self.history[index][-1][1] = val
        else:
            # add new item
            self.history[index].append([self.id, val])

    # Time: O(1)
    def snap(self) -> int:
        self.id += 1
        return self.id - 1

    # Time: O(logn)
    def get(self, index: int, snap_id: int) -> int:
        # get the most recent call from snap_id - bisect_right
        last_ind = bisect_right(
            self.history[index], snap_id, key=lambda x: x[0])
        return self.history[index][last_ind - 1][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
