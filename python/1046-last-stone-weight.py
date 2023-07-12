class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        Time: O(nlogn) ; (n) heapify a list 
                  ; go through the entire stone stack is (n) b/c youre always destroying stone X or 
                  sometimes destroying stone Y to speed up the process 
                  ;     - adding back into the heap is (logn)
                  ; O(n + nlogn)
        Space: O(n) ; given list and the heap
        '''

        stones = [-1 * stone for stone in stones]
        heapq.heapify(stones)
        # stack of stones
        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)

            y = y - x
            if y != 0:
                heapq.heappush(stones, y)

        return abs(stones[0]) if len(stones) != 0 else 0
