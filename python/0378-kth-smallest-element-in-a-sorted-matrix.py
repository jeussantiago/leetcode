class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        '''
        - theres no gurantee that the next row is greater than the last ind of the the current row
        - Ex: [1,5,9],[4,6,10]

        min Heap:
        Time: O(n^2)
        Space: O(k)
        '''
        n = len(matrix)
        maxHeap = []
        heapq.heapify(maxHeap)
        for i in range(n):
            for j in range(n):
                if len(maxHeap) >= k:
                    if -matrix[i][j] > maxHeap[0]:
                        heapq.heappop(maxHeap)
                        heapq.heappush(maxHeap, -matrix[i][j])
                else:
                    heapq.heappush(maxHeap, -matrix[i][j])

        return -heapq.heappop(maxHeap)
