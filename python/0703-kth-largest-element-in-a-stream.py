class KthLargest:
    '''
    __init__:
    T: O(logn) ; add function
    S: O(n) ; heap

    add:
    T: O(logn) ; O(logn + logn) pop and push
    S: O(n) ; heap
    '''

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = []

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.minHeap) == self.k:
            if val > self.minHeap[0]:
                heapq.heappop(self.minHeap)
                heapq.heappush(self.minHeap, val)
        else:
            heapq.heappush(self.minHeap, val)

        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
