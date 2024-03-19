class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        Max Heap and Queue

        ["A","A","A","A","B","B","C","D"]

        - create counter
        {
            A: 4
            B: 2
            C: 1
            D: 1
        }

        - you want a a max heap from this counter
            - store as [(freq, letter)]
        => [(4, A), (2, B), (1, C), (1, D)]

        - pop the top of the maxHeap
                - this is going to our first letter in the sequence
                - update the sequence length (+1)
            => [(2, B), (1, C), (1, D)]
            - add the letter to the queue with reduced value
                ** if the value is 0, don't add, this means that we
                ran out of that letter
                - we need to keep track of when we added the letter
                in the sequence. we can do this by keeping track
                of the current sequence count when added. that way we
                can just check the difference between the added 
                sequence count and the current sequence count to see
                if n cooling time has passed
            => q = [(3, A)]

        - if the length of the queue is the same as N
            - pop the front of the queue
            - add back into maxHeap 

        - continuously repeat this process until both maxHeap
        and queue are empty

        n is the length of tasks array
        k is the cooling time
        Time: O(n)
            ; (1) create counter dict - only 26 letters
            ; (1) convert counter dict to heap - only 26 letters
            ; (n)iterate through heap
            ; (logk = log1 = 1) pop from heap - heap can only be as long as k, which is 26 max
            ; (logk = log1 = 1) add back to heap
        Space: O(1)
            ; (1) dict - only 26 letters
            ; (1) heap - only 26 letters
        '''

        cnt = collections.Counter(tasks)
        # don't need the letters
        maxHeap = [-freq for freq in cnt.values()]
        heapq.heapify(maxHeap)
        q = collections.deque()
        sequence_len = 0
        while maxHeap or q:

            sequence_len += 1

            if maxHeap:
                freq = heapq.heappop(maxHeap) + 1
                if freq != 0:
                    next_avaialble_insert_time = sequence_len + n
                    q.append((next_avaialble_insert_time, freq))

            if q and q[0][0] == sequence_len:
                _, freq = q.popleft()
                heapq.heappush(maxHeap, freq)

        return sequence_len
