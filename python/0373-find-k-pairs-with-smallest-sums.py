class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        '''
        Min Heap:
        - have to keep track of the next number

        nums1 = [1,2,11]
        nums2 = [3,4,6]
        [[1,3],[1,4],[2,3],[2,4],[1,6],[2,6],[3,11],[4,11],[6,11]]

        - (0,0) is in heap
            - add to heap
        - now add (0,1) and (1,0) to minheap
        - whatever is on top is the min val - in this instance they have the same val lets just say (0,1) was popped
        - now we still have (1,0) in the heap but we need to add the next set of numbers to compare it to
        - popped wal => (i,j) = (0,1)
        - add (i, j + 1) and (i + 1, j) => (0,2) and (1,1)

        - popped (i,j) = (1,0)
        - add (2,0) but we can't add (1,1) since its already been added to the heap or was added before

        if j < len(nums2) and (i, j + 1) not seen
            add (i, j + 1)
        if i < len(nums1) and (i, j + 1) not seen
            add (i, j + 1)

        m is len of nums1
        n is len of nums2
        Time: min(klogk, m*nlog(m*n)) 
                ; iterate through min(k, m * n)
                ; min(klogk, m*nlog(m*n)) add indexes to heap (logn)
                ; at each iteration, we add 2 pairs but pop 1, since the heap can grow to size min(k, m * n), we need to 
                ; insert into heap which is (log)
        Space: min(k, m * n) 
                ; visited set and heap can grow to this size
        '''
        M, N = len(nums1), len(nums2)

        minHeap = [(nums1[0] + nums2[0], 0, 0)]
        heapq.heapify(minHeap)
        seen = set()

        res = []
        while k > 0 and minHeap:
            val, i1, i2 = heapq.heappop(minHeap)
            res.append([nums1[i1], nums2[i2]])

            if i1 + 1 < M and (i1 + 1, i2) not in seen:
                # (total, nums1_ind, nums2_ind)
                tup = (nums1[i1 + 1] + nums2[i2], i1 + 1, i2)
                heapq.heappush(minHeap, tup)
                seen.add((i1 + 1, i2))

            if i2 + 1 < N and (i1, i2 + 1) not in seen:
                tup = (nums1[i1] + nums2[i2 + 1], i1, i2 + 1)
                heapq.heappush(minHeap, tup)
                seen.add((i1, i2 + 1))

            k -= 1

        return res
