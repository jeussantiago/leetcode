class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        '''
        Min Heap

        - sort by the start date
        [[1, 2], [1, 2], [1, 5], [1, 5], [3, 3]]

        - get the max number of days the events will take place (in the example above: 5)

        - iterate through the days
            - since events array is increasing, we can check the start date of the current ith event
            and add its end date the the min Heap if the start date is <= to the current day

            - some events may have finished
                - pop the values on the top of the min heap if their end_date is < current date

            - if there is an item in the minheap, this means that you can attend this event
                - increse count +1
                - pop top item from minheap



        n is the length of events
        d is the total number of days in the event
        Time: O(nlogn)
            ; (nlogn) sorting
            ; (d) iterate over days
            ; (n * logn) push end_date onto heap
            ; (n * logn) removing item from min Heap
                {n multiplication is b/c we have to do it for every event}

        Space: O(n)
            ; (n) sorting
            ; (n) minheap
        '''

        events.sort()

        res = 0
        maxDays = max(end_date for _, end_date in events)
        minHeap = []
        i = 0

        for currDay in range(1, maxDays + 1):
            while i < len(events) and events[i][0] <= currDay:
                # push end date
                heapq.heappush(minHeap, events[i][1])
                i += 1

            # some events finished already
            while minHeap and minHeap[0] < currDay:
                heapq.heappop(minHeap)

            # attend event if available
            if minHeap:
                heapq.heappop(minHeap)
                res += 1

        return res
