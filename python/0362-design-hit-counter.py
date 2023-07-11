class HitCounter:
    '''
    Queue:
    [1,2,3,300,302]
    - pop the front of the queue until the front is less than 300s from the back
    - taking advantage of the fact that the calls are going to be made in cronological order so we don't care about the porevious hits before 300s
    while q[0] - q[-1] >= 300:
        - pop from queue

    __init__:
    - initialize queue

    hit:
    - add the timestamp to the back of the queue

    T: O(1)
    S: O(n)

    getHits:
    - remove the front of the queue until it is no longer 300s behind

    T: O(n) ; where n is the number of hits recorded so far
    S: O(n)

    '''

    def __init__(self):
        self.q = collections.deque()

    def hit(self, timestamp: int) -> None:
        self.q.appendleft(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.q and timestamp - self.q[-1] >= 300:
            self.q.pop()

        return len(self.q)


class HitCounter:
    '''
    Binary search method
    - store all the hits
    - when you call getHit
        - you use binary search to find where the current timestamp will be placed 300s in the past

    hit:
    T: O(1)
    S: O(n)

    gethit:
    T: O(logn)
    S: O(n)

    '''

    def __init__(self):
        self.q = []

    def hit(self, timestamp: int) -> None:
        self.q.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        ind = bisect_right(self.q, timestamp - 300)
        return len(self.q) - ind


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
