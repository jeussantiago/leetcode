class ZigzagIterator:
    '''
    __init__
    Time: O(k * n) where k is the number of list and n is the max list size
        : in this specific case since k == 2, O(2n) == O(n) or O(m + b) where m and b are len of v1 and v2
    Space: O(k * n)

    next
    Time: O(1)
    Space: O(k * m)

    hasNext
    Time: O(1)
    Space: O(k * m)
    '''

    def __init__(self, v1: List[int], v2: List[int]):
        self.zigzag = []
        lsts = [v1, v2]
        for i in range(max(len(v1), len(v2))):
            for lst in lsts:
                if i >= len(lst):
                    continue
                self.zigzag.append(lst[i])

    def next(self) -> int:
        if self.hasNext():
            return self.zigzag.pop(0)

    def hasNext(self) -> bool:
        return self.zigzag


class ZigzagIterator:

    '''

    __init__
    - only add list with items to queue
    Time: O(k) where k is the number of list, in this case 2
    Space: O(k) 

    next
    Time: O(1)
    Space: O(k)

    hasNext
    Time: O(1)
    Space: O(k)

    '''

    def __init__(self, v1: List[int], v2: List[int]):
        self.zigzag = [v1, v2]
        self.queue = collections.deque()
        for i, vector in enumerate(self.zigzag):
            if vector:
                # index of vector and vector iterator
                self.queue.appendleft((i, 0))
        print(self.queue)

    def next(self) -> int:
        if self.hasNext():
            zigzag_idx, vector_idx = self.queue.pop()
            # add back to end of queue with increased index
            if vector_idx < len(self.zigzag[zigzag_idx])-1:
                self.queue.appendleft((zigzag_idx, vector_idx+1))
            # return the popped element
            return self.zigzag[zigzag_idx][vector_idx]

    def hasNext(self) -> bool:
        return self.queue


# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
