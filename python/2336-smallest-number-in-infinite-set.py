class SmallestInfiniteSet:
    '''
    heap and set

    __init__:
    - create curr_val
    - create minHeap
    - create set


    T: O(1)
    S: O(1)

    popSmallest:
    - the values in the minHeap will always be smaller than the smallest_val
    - this is because, you have to continously pop from the infinite set tot increase teh smallest_val
    and the only values being pushed in the heap and values < the smallest_val

    - so if a heap exist, this means there is a value smaller than the smallest_val that does exist in the infinite set
        - remove the item from the min Heap
        - remove item from set
        - return min Heap popped item
    - there are no items in the heap which means no items smaller than smallest_val
        - save curr_val in temp val
        - increament curr_val
        - return temp val


    T: O(logn)
    S: O(n)

    addBack:
    - minHeap and set stores the values added back into the heap

    - if num in set/minHeap ; we can also ignore any num > curr_val since those numbers still exist in the infinite set
        - ignore
    - if num not in set/minHeap
    ( these are the numbers that were popped before but we need to know that they exist again)
        - push the num into the min Heap
        - push the num into the set

    T: O(logn)
    S: O(n)

    '''

    def __init__(self):
        self.smallest_val = 1
        self.minHeap = []
        heapq.heapify(self.minHeap)
        self.existing_nums = set()

    def popSmallest(self) -> int:
        if self.minHeap:
            val = heapq.heappop(self.minHeap)
            self.existing_nums.remove(val)
            return val

        else:
            self.smallest_val += 1
            return self.smallest_val - 1

    def addBack(self, num: int) -> None:
        if (
            num >= self.smallest_val or
            num in self.existing_nums
        ):
            return

        # keep a record of the num to mention that this num exist in the infinite set once again
        heapq.heappush(self.minHeap, num)
        self.existing_nums.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
