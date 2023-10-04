class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        '''
        n is the length of nums
        Time: O(nlogk)
            ; (n) go through all the numbers
            ; (logk) pop and add from heaps
        Space: O(n)
            ; (k) each heap requires k//2 space
            ; (n) hashmap requires space for all the numbers in the list except the last 3
        '''

        maxHeap, minHeap = [], []  # nums <= median, nums > median
        maxHeapSize, minHeapSize = 0, 0
        deleteNumsMap = collections.defaultdict(int)
        res = []

        def getMedian():
            if k % 2 == 0:
                return (-maxHeap[0] + minHeap[0]) / 2.0
            else:
                return maxHeap[0] * -1.0

        # fill initial maxHeap
        for i in range(k):
            heappush(maxHeap, -nums[i])
            maxHeapSize += 1

        # fill initial minHeap - we take the values from maxHeap since those values are sorted
        for i in range(k//2):
            heappush(minHeap, -heappop(maxHeap))
            maxHeapSize -= 1
            minHeapSize += 1

        # get the first median
        res.append(getMedian())

        # insert the other numbers in the list
        for ind in range(k, len(nums)):
            # decide where the current number belongs, in the minHeap if the num > median otherwise, the num goes into the maxHeap
            # maxHeap are numbers < median
            num = nums[ind]
            median = getMedian()
            if num > median:
                heappush(minHeap, num)
                minHeapSize += 1
            else:
                heappush(maxHeap, -num)
                maxHeapSize += 1

            # when we move the pointer, we need to keep track of that number to be deleted, so that if we encounter it later on, we
            # can remove this number for the minHeap or maxHeap
            # ind - k represents the left pointer
            numToDelete = nums[ind - k]
            deleteNumsMap[numToDelete] += 1

            # Since we know the top/median values of the heap, we know where the number that is going to be deleted is located
            # if deletedNumber < median/top of maxHeap, then we keep track of that by lowering the size of maxHeap
            # same concept with minHeap
            if numToDelete <= -maxHeap[0]:
                maxHeapSize -= 1
            else:
                minHeapSize -= 1

            # need to balance the sizes of the heaps, if maxHeap has more values, then move values from the maxHeap to the minHeap and adjust sizes
            # same concept with minHeap
            if maxHeapSize - minHeapSize > 1:
                heappush(minHeap, -heappop(maxHeap))
                maxHeapSize -= 1
                minHeapSize += 1
            elif minHeapSize > maxHeapSize:
                heappush(maxHeap, -heappop(minHeap))
                maxHeapSize += 1
                minHeapSize -= 1

            # check both heaps for the number to be deleted
            # only check the top values
            # the dictionary will contain a count of the number of instances of the number to be deleted so just keep popping until the value reaches 0
            while maxHeap and deleteNumsMap[-maxHeap[0]] > 0:
                deleteNumsMap[-maxHeap[0]] -= 1
                heappop(maxHeap)

            while minHeap and deleteNumsMap[minHeap[0]] > 0:
                deleteNumsMap[minHeap[0]] -= 1
                heappop(minHeap)

            # record the median
            res.append(getMedian())

        return res
