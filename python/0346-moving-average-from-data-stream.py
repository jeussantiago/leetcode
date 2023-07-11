class MovingAverage:
    '''
    Queue
    n is the max_size
    Time: O(1)
    Space: O(n)
    '''

    def __init__(self, size: int):
        self.max_size = size
        self.q = collections.deque()
        self.total = 0

    def next(self, val: int) -> float:
        if len(self.q) == self.max_size:
            self.total -= self.q.pop()

        self.q.appendleft(val)
        self.total += val
        avg = self.total / len(self.q)
        return avg


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
