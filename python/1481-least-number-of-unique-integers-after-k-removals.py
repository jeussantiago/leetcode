class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        '''
        Min Heap
        (not really) 
        - more like, sorting the frequencies

        Time: O(nlogn)
        Space: O(n)
        '''

        cnt = collections.defaultdict(int)
        for num in arr:
            cnt[num] += 1

        minHeap = [(freq, num) for num, freq in cnt.items()]

        sorted_minHeap = sorted(minHeap, key=lambda x: x[0])
        heap_len = len(sorted_minHeap)
        i = 0
        while i < heap_len and k - sorted_minHeap[i][0] >= 0:
            k -= sorted_minHeap[i][0]
            i += 1

        return heap_len - i
