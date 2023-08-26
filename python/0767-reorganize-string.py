class Solution:
    def reorganizeString(self, s: str) -> str:
        '''
        Heaps
        {
            a: 4
            b: 3
            c: 2
            d: 1
        }

        - keep track of the top two highest values in the heap
        - we need a max heap but python only has min heaps so we multiply the values by -1

        - at each position, check the previous char
            - if the previous char == max_heap_top_char
                - pop from the heap (removes char/count from there)
                - pop from the heap (char to add to the string)

                - add first pop back into heap
                - add second pop back into heap with count -1 (unless count == 0)

            - else
                - pop for heap
                - add char to string
                - add char back to heap with -1 count (unless count == 0)

        n is the length of s
        k is the number of unique letters
        Time: O(nlogk)
            ; (n) create Counter
            ; (log k) pop from heap
            ; (log k) add back to heap
            ; (n * (logk + logk)) we do this process with the heap for all positions in the string
        Space: O(k)
            ; (k) Counnter dict
            ; (k) heap
        '''

        s_counter = collections.Counter(s)
        maxHeap = [(-1 * count, char)for char, count in s_counter.items()]
        heapq.heapify(maxHeap)

        res = ""
        while maxHeap:
            first_count, first_char = heapq.heappop(maxHeap)

            # first char in the string or check if not repeating char
            if not res or res[-1] != first_char:
                res += first_char
                if first_count + 1 != 0:
                    heapq.heappush(maxHeap, (first_count + 1, first_char))

            else:
                # previous character was repeating which means that there are no more characters to add
                if not maxHeap:
                    return ""

                # repeating char, add the second char instead
                sec_count, sec_char = heapq.heappop(maxHeap)
                res += sec_char
                if sec_count + 1 != 0:
                    heapq.heappush(maxHeap, (sec_count + 1, sec_char))
                # add the back the first char
                heapq.heappush(maxHeap, (first_count, first_char))

        return res
