class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        '''
        - store each visited number into a maxHeap.

        - while the current number is > than the top of the heap, pop from the heap
        - add the length of the heap to the count of the nums

        nums = [1,4,2,5,3]
        maxHeap = [1] ; count = 1
        maxHeap = [1,4] ; count = 3
        maxHeap = [1,2] ; count = 5
        - 4 was popped b/c it is > than 2
        maxHeap = [1,2,5] ; count = 8
        maxHeap = [1,2,3] ; count = 11

        nums = [2,2,2]
        maxHeap = [2] ; count = 1
        maxHeap = [2,2] ; count = 3
        maxHeap = [2,2,2] ; count = 6

        Time: O(nlogn)
            ; (n) go through each numn
            ; (logn) each num is added onto the maxHeap
            ; (logn) each num can be removed from the maxHeap
            ; (n * (logn + logn))
        Space: O(n)
            ; (n) at most in the maxHeap, we an have the entire nums list
        '''
        res = 0
        maxHeap = []
        for num in nums:

            while maxHeap and abs(maxHeap[0]) > num:
                heappop(maxHeap)

            heappush(maxHeap, num * -1)
            res += len(maxHeap)

        return res
