class MedianFinder:
    '''
    Heap:
    - adding to a heap is O(logn) -> height of tree
    - removing from a heap is O(logn) -> height of tree

    - with a max heap, finding the max is O(1)
    - with a min heap, finding the min is O(1)
        => just look at the first root/element

    - Use 2 heaps
        - max heap to represent the number <= mid
        - min heap to represent the number >= mid
        max heap = [1,2]
        min heap = [3,4]

    - if they're even in size, then we can take the max of the max heap and the min of the min heap,
    add them and divid by 2 -> (2 + 3) / 2
    - if they're uneven in size, the larger of the two is our median
        max heap = [0,1,2]
        min heap = [3,4]
        - the <= heap is bigger than the other heap, this means the max value in teh max heap is the mid

    - so the challenge is to keep each heap the same size or atleast 1 size difference away from each other
    - python only implements minHeaps, to tackle the maxHeap issue, we can just multiple each number by -1
        - maxHeap = [-4,-3,-2]
        - minHeap = [2,3,4]


    [2,1]
    [3,4]


    '''

    def __init__(self):
        # Time: O(1)
        # Space: O(1)
        # python only implements minHeaps, to tackle the maxHeap issue, we can just multiple each number by -1
        self.left = []  # maxHeap (multiply by -1)
        self.right = []  # minHeap

    def addNum(self, num: int) -> None:
        # Time: O(logn)
        # Space: O(n)
        if self.right and num > self.right[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, num * -1)

        # make sure that every element in leftHeap <= every element in rightHeap
        if len(self.left) > len(self.right) + 1:
            val = heapq.heappop(self.left) * -1
            heapq.heappush(self.right, val)

        if len(self.right) > len(self.left) + 1:
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, val * -1)

        # if len(self.left) == len(self.right):
        #     heapq.heappush(self.left, num * -1)
        #     val = heapq.heappop(self.left) * -1
        #     heapq.heappush(self.right, val)

        # else:
        #     heapq.heappush(self.right, num)
        #     val = heapq.heappop(self.right)
        #     heapq.heappush(self.left, val * -1)

    def findMedian(self) -> float:
        # Time: O(1)
        # Space: O(n) where n is the number of nums added to the list
        # print(self.left)
        # print(self.right)
        # print('--------')
        if len(self.left) == len(self.right):
            # even length => [1,2,3,4]
            return ((self.left[0] * -1) + self.right[0]) / 2
        else:
            # odd length => [1,2,3]
            if len(self.left) > len(self.right):
                print(self.left[0])
                return self.left[0] * -1
            else:
                return self.right[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
