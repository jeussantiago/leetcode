class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        '''
        - set
        - create a heap
        - pull out the max 3 times
        Time: O(2n + 3logn) => O(n)
        Space: O(1) ; at most there are going to be 3 values in the minHeap and in the set

        '''
        minHeap = []
        exist = set()
        for num in nums:
            if num not in exist:
                if len(minHeap) < 3:
                    heapq.heappush(minHeap, num)
                    exist.add(num)
                else:
                    # new number has greater value than whats in the heap
                    if num > minHeap[0]:
                        val = heapq.heappop(minHeap)
                        exist.remove(val)

                        heapq.heappush(minHeap, num)
                        exist.add(num)

        # if there are not 3 distinct elements, return the highest value
        if len(minHeap) < 3:
            return minHeap[-1]

        return minHeap[0]
