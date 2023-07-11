class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        '''

        priority queues and counter

        - add items to the heap based on the counter of the char
        - require a max Heap
        - items with bigger counts in the heap should be placed in the string first
        - go until k so you can seperate each char by the distance required
        - after each k, you should reevaluate
        s = "aaadbbcc", k = 2
        {'a': 3, 'b': 2, 'c': 2, 'd': 1}
        ans = ab
        - after k=2 inserts, reevaluate maxheap order
            - after insert a char, pop the item from the heap, and reduce the count
            - after k iterations
                - if count > 0: add back into the heap
        {'a': 2, 'b': 1, 'c': 2, 'd': 1}
        ans = abac
        {'a': 1, 'b': 1, 'c': 1, 'd': 1}
        ans = abacab
        {'a': 0, 'b': 0, 'c': 1, 'd': 1}
        ans = abacabcd
        {'a': 0, 'b': 0, 'c': 0, 'd': 0}
        ans = abacabcd

        - in each iteration, if there aren't enough items in the heap to fill k distance before going back to the same char, then not possible
        s = "aaabc", k = 3
        {'a': 3, 'b': 1, 'c': 1}
        ans = abc
        {'a': 2, 'b': 0, 'c': 0}
        ans = abc
        - issue here is that there is only 1 item in the heap and theres still another a to add
            - would be fine if it was {'a': 1, 'b': 0, 'c': 0} since we can just add teh last 'a'
            but in {'a': 2, 'b': 0, 'c': 0} its not fine since we can't seperate the 'a' by k distance

        - before each insert group, we can check if the length of the heap is < k, if len(heap) < k and any(count in heap is > 1) => return false
        - proceed noramlly if len(heap) < k and al(count in heap is <= 1)
            - since we are working with a maxHeap, we don't need to check the entire heap to see if any count > 1, we can just check the the top 
            of the heap since that will have the biggest count

        Time: O(nlogn) ; go to each character and insert back into the heap
        Space: O(n) ; heap and counter
        '''
        if k == 0:
            return s

        # get the counter
        count = collections.Counter(s)

        # heapify
        maxHeap = [(-freq, c) for c, freq in count.items()]
        heapq.heapify(maxHeap)

        res = ""
        # loop through heap
        while maxHeap:
            # check if the heap contains enough numbers to seperate chars at k distance
            if len(maxHeap) < k and maxHeap[0][0] < -1:
                return ""

            # get the top k items from heap to add to the results
            q = []
            for _ in range(k):
                if not maxHeap:
                    break
                q.append(heapq.heappop(maxHeap))

            # add the items back into the heap with count reduced
            for freq, c in q:
                res += c
                if freq + 1 < 0:
                    heapq.heappush(maxHeap, (freq + 1, c))

        return res
